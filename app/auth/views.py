from flask import render_template
from . import auth
from flask_login import login_required, login_user
from ..models import User
from .forms import LoginForm, RegistrationForm
from .. import db
from ..email import send_email

@auth.route('/login')
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return render_template('auth/login.html')

    