# Import needed modules
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField, BooleanField
from wtforms.validators import DataRequired, URL


# Create database
class Base(DeclarativeBase):
    pass


# Initiate Flask instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

app.config['SECRET_KEY'] = 'the_secret_key'
Bootstrap5(app)


# Cafe table configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    # Function to convert data into dictionary format
    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


# Initialize database
with app.app_context():
    db.create_all()


# Make a class for the form
class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    map_url = URLField('Location URL', validators=[URL()])
    img_url = URLField('Image URL', validators=[URL()])
    location = StringField('Location', validators=[DataRequired()])
    seats = SelectField('Number of seats',
                        choices=[('0-10', '0-10'), ('10-20', '10-20'), ('20-30', '20-30'),
                                 ('30-40', '30-40'), ('40-50', '40-50'), ('50+', '50+')],
                        validators=[DataRequired()])
    coffee_price = StringField('Coffee price', validators=[DataRequired()])
    has_sockets = BooleanField('Has sockets?')
    has_toilet = BooleanField('Has toilets?')
    has_wifi = BooleanField('Has wi-fi?')
    can_take_calls = BooleanField('Can take calls?')
    submit = SubmitField('Submit', render_kw={"class": "btn btn-warning mt-3"})


# Define home page
@app.route("/")
def home():
    return render_template("index.html")


# Define a page that shows all the Cafes listed in the database
@app.route('/cafes', methods=["GET"])
def cafes():
    # Pass a list of unique locations to the HTML
    loc_query = db.session.query(Cafe.location).distinct().order_by(Cafe.location.asc())
    unique_locations = [loc[0] for loc in loc_query.all()]

    # Filter out the cafe DB by the selected filters
    filtered_list = db.select(Cafe)
    if request.args.get("wifi"):
        filtered_list = filtered_list.where(Cafe.has_wifi == True)
    if request.args.get("sockets"):
        filtered_list = filtered_list.where(Cafe.has_sockets == True)
    if request.args.get("toilet"):
        filtered_list = filtered_list.where(Cafe.has_toilet == True)
    if request.args.get("calls"):
        filtered_list = filtered_list.where(Cafe.can_take_calls == True)

    selected_neighbourhoods = request.args.getlist("neighbourhood")
    if selected_neighbourhoods:
        filtered_list = filtered_list.where(Cafe.location.in_(selected_neighbourhoods))

    cafes_list = db.session.execute(filtered_list).scalars().all()
    all_cafes = []
    for cafe in cafes_list:
        new_cafe = cafe.to_dict()
        all_cafes.append(new_cafe)
    return render_template('cafes.html', cafes=all_cafes, locations=unique_locations)


# Define a way to delete a given cafe
@app.route("/delete-cafe/<int:cafe_id>", methods=["POST"])
def delete_cafe(cafe_id):
    cafe_to_delete = db.get_or_404(Cafe, cafe_id)
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return redirect(url_for('cafes'))


# Define a page to add a new row into the cafe data
@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            location=form.location.data,
            has_wifi=form.has_wifi.data,
            has_sockets=form.has_sockets.data,
            has_toilet=form.has_toilet.data,
            can_take_calls=form.can_take_calls.data,
            seats=form.seats.data,
            coffee_price=form.coffee_price.data,
            img_url=form.img_url.data,
            map_url=form.map_url.data
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


# Run the flask app
if __name__ == '__main__':
    app.run(debug=True)
