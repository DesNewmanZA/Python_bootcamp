# Import needed modules
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


# Make a class for the registration form, taking in email and password, with password confirmation
class RegistrationForm(FlaskForm):
    email = StringField(
        "Email", validators=[DataRequired(), Email(), Length(max=120)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6)]
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")


# Make a class for the login form, taking in email and password
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
