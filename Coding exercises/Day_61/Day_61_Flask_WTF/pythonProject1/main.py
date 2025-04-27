# Import needed modules
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, Length
from flask_bootstrap import Bootstrap5


# Make logins class
class UserLogin(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message="Invalid email address")])
    password = PasswordField(label='Password', validators=[
        DataRequired(),
        Length(min=8, message="Password must be minimum 8 characters!")])
    submit = SubmitField(label='Log in')


# Initiate flask instance
app = Flask(__name__)
app.secret_key = "my_secret_key"
bootstrap = Bootstrap5(app)

# Define home page
@app.route("/")
def home():
    return render_template('index.html')


# Define login page
@app.route("/login", methods=['GET', 'POST'])
def login():
    logins = UserLogin()
    if logins.validate_on_submit():
        if logins.email.data == 'admin@email.com' and logins.password.data == '12345678':
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=logins)



# Run server
if __name__ == '__main__':
    app.run(debug=True)
