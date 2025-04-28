# Import needed modules
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError


# Define the Flask app
app = Flask(__name__)

# Create and configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()


# Define a model (table)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(), nullable=False)


# Define home page
@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template('index.html', books=all_books)


# Define add book page
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=float(request.form["rating"])
        )
        db.session.add(new_book)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return "A book with that title already exists!"
        return redirect(url_for('home'))
    return render_template('add.html')


# Define edit rating page
@app.route("/edit/<book_id>", methods=["GET", "POST"])
def edit(book_id):
    selected_book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()

    if request.method == "POST":
        new_rating = float(request.form["rating"])
        selected_book.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', book=selected_book)


# Define deletion of book page
@app.route("/delete/<book_id>")
def delete(book_id):
    selected_book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(selected_book)
    db.session.commit()
    return redirect(url_for('home'))


# Run Flask site
if __name__ == "__main__":
    app.run(debug=True)
