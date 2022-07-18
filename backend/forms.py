from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import length
from wtforms.validators import equal_to
from wtforms.validators import email
from wtforms.validators import data_required
from wtforms.validators import ValidationError
from backend.db_modeles import User



class RegisterForm(FlaskForm):

    """First Level of validation against the existing records in the database"""
    # This method verifies if the given username already exists in the database
    def validate_username(self, username_for_checking):
        user = User.query.filter_by(username=username_for_checking.data).first()
        if user:
            raise ValidationError("This username is not available, please try choosing a different username")

    # This method verifies if the given email address already exists in the database
    def validate_email_address(self, email_for_checking):
        user = User.query.filter_by(email_address=email_for_checking.data).first()
        if user:
            raise ValidationError("This email address is not available, please try choosing a different email address")

    """Second Level of validation against the form requirements"""
    username = StringField(label='User Name:', validators=[length(min=4, max=32), data_required()])
    email_address = StringField(label='Email:', validators=[email(), data_required()])
    password = PasswordField(label='Password:', validators=[length(min=8, max=64), data_required()])
    password_confirmation = PasswordField(label='Confirm Password:', validators=[equal_to('password'), data_required()])
    submit = SubmitField(label='Register')


class LoginForm(FlaskForm):

    username = StringField(label='User Name:', validators=[data_required()])
    password = PasswordField(label='Password:', validators=[data_required()])
    submit = SubmitField(label='Log in')

