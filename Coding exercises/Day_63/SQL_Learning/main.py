from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Make a flask instance
app = Flask(__name__)


# Create and configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)


# Define a model (table)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(), nullable=False)


with app.app_context():
    db.create_all()
    new_book = Book(title="some title 3", author="d newman", rating=9)
    db.session.add(new_book)
    db.session.commit()
