from wtforms import Form, StringField, BooleanField, TextAreaField, PasswordField, validators
from . import main

class LoginForm(Form):
	openid = StringField('openid', validators=[validators.DataRequired()])
	remember_me = BooleanField('remember_me',default=False)

class RegisterForm(Form):
    username = StringField('Username', [validators.Length(min=1, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')
		