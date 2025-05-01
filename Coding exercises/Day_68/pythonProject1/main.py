# Import needed modules
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

# Create a flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'


# Create database of users
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Start a login manager and make a user loader callback
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


# Create table in database
with app.app_context():
    db.create_all()


# Define home page
@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


# Define registration page
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check to see if user already exists
        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        # If user doesn't exist, register them
        new_user = User(
            name=request.form.get("name"),
            email=request.form.get("email"),
            password=generate_password_hash(request.form.get("password"), method="pbkdf2:sha256", salt_length=8))
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        return redirect(url_for("secrets"))
    return render_template("register.html", logged_in=current_user.is_authenticated)


# Define login page
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Try to log in
        email = request.form.get('email')
        password = request.form.get('password')
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        # If user doesn't exist
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        # If password is incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        # Else login
        else:
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html", logged_in=current_user.is_authenticated)


# Define secrets page
@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


# Define logout page
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


# Define download page
@app.route('/download', methods=['POST'])
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


# Run flask app
if __name__ == "__main__":
    app.run(debug=True)
