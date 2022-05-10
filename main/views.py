from email import message
from flask import render_template
from . import main
from flask_login import login_required

@main.route('/')
def index():
    message = "welcome to the main page"
    return render_template('index.html', message=message)

    