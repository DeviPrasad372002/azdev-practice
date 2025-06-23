#new line add
from flask import Flask, render_template, request
import re

app = Flask(__name__)

def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        errors.append("Password must contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        errors.append("Password must contain at least one lowercase letter.")
    if not re.search(r"\d", password):
        errors.append("Password must contain at least one digit.")
    if not re.search(r"[!@#$%^&*()]", password):
        errors.append("Password must contain at least one special character (!@#$%^&*()).")

    return errors

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    errors = []

    if request.method == 'POST':
        password = request.form['password']
        errors = validate_password(password)

        if not errors:
            message = "Password is valid! ✅"

    return render_template('index.html', message=message, errors=errors)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

