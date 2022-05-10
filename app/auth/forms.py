from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, Length, Email, EqualTo
from ..models import User
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    username = StringField('Enter your username', validators=[Required(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[Required(), Length(min=4, max=25)])
    confirm_password = PasswordField('Confirm Password', validators=[Required(), EqualTo('password')])
    EqualTo('password2') ,message = 'Passwords must match'
    password2 = PasswordField('Confirm Password', validators=[Required(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    