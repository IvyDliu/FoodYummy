from wtforms import Form, StringField, BooleanField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from . import auth
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
    email = StringField(validators=[Required(), Length(1, 64),Email()])
    password = PasswordField(validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

    # def validate_login(self, field):
    #     user = self.get_user()

    #     if user is None:
    #         raise validators.ValidationError('Invalid user')

    #     if user.password != self.password.data:
    #         raise validators.ValidationError('Invalid password')

    def get_user(self):
        return User.objects(email=self.email.data).first()

class RegisterForm(Form):
    email = StringField('Email', validators=[Required("Please enter your email address."), Length(1, 64),
Email("Please enter your email address.")])
    username = StringField("Username", validators=[Required(), Length(1,50), Regexp('^[A-Za-z][A-Za-z0-9_]*$', 0,
'Usernames must have only letters, numbers, or underscores')])
    password = PasswordField("Password",validators=[Required(),EqualTo("confirm", message="Passworld do not match")])

    confirm = PasswordField("Confirm Password")
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.objects(email=self.email.data).first():
            raise ValidationError('Email already registered.')	
            
class EditProfileForm(Form):
	new_name = StringField('Enter A New Name',validators=[Required(), Length(1,50), Regexp('^[A-Za-z][A-Za-z0-9_]*$', 0,
'Usernames must have only letters, numbers, or underscores')])
	password = PasswordField("Password",validators=[Required(),EqualTo("confirm", message="Passworld do not match")])
	confirm = PasswordField("Confirm Password")
	submit = SubmitField('Update')
		