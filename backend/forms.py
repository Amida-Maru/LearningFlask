from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label='User Name:')
    email_address = StringField(label='Email:')
    password = PasswordField(label='Password:')
    password_confirmation = PasswordField(label='Confirm Password:')
    submit = SubmitField(label='Register')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:')
    password = PasswordField(label='Password:')
    submit = SubmitField(label='Login')
