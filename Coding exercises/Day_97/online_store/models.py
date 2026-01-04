# Import needed modules
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# Start DB instance
db = SQLAlchemy()


# Create a user class to store their unique ID, email and password
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)


# Create a product class to store product unique IDs, names, description, price and images
class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price_cents = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255))
