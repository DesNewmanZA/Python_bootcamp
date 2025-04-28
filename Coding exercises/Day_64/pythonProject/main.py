# Import needed modules
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from sqlalchemy.exc import IntegrityError

# Define static variables
MOVIE_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_ID_URL = "https://api.themoviedb.org/3/movie/"
API_KEY = 'myapikey'

# Create a flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'asecretkey'
Bootstrap5(app)

# Create a movie DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-list.db'
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()


# Define a model (table)
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    year = db.Column(db.Integer)
    description = db.Column(db.String(1000))
    rating = db.Column(db.Float())
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), nullable=False)


class RateMovieForm(FlaskForm):
    rating = StringField(u'Your rating out of 10', validators=[DataRequired()])
    review = StringField(u'Your review')
    submit = SubmitField('Submit', render_kw={"class": "btn mt-3"})

class AddMovieForm(FlaskForm):
    title = StringField(u'Movie name:', validators=[DataRequired()])
    submit = SubmitField('Add movie', render_kw={"class": "btn mt-3"})

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/edit/<movie_id>", methods=['GET', 'POST'])
def edit(movie_id):
    form = RateMovieForm()
    selected_movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    if form.validate_on_submit() and request.method == "POST":
        selected_movie.rating = form.rating.data
        selected_movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", movie=selected_movie, form=form)


# Define deletion of movie page
@app.route("/delete/<movie_id>")
def delete(movie_id):
    selected_movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    db.session.delete(selected_movie)
    db.session.commit()
    return redirect(url_for('home'))


# Define add movie page
@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if request.method == "POST" and form.validate_on_submit():
        new_movie_title = request.form["title"]
        params = {
            'api_key': API_KEY,
            'query': new_movie_title
        }
        response = requests.get(MOVIE_SEARCH_URL, params=params)
        data = response.json()["results"]
        return render_template('select.html', movies=data)
    return render_template('add.html', form=form)


# Define selection of movie page
@app.route("/select/<movie_id>")
def select(movie_id):
    params = {
        'api_key': API_KEY,
        'language': 'en-US'
    }
    response = requests.get(f"{MOVIE_ID_URL}{movie_id}", params=params)
    data = response.json()
    new_movie = Movie(
        title=data['title'],
        year=int(data['release_date'].split("-")[0]),
        description=data['overview'],
        img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
        rating=5,
        review="",
        ranking=5
    )
    db.session.add(new_movie)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return "A movie with that title already exists!"
    return redirect(url_for('edit', movie_id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
