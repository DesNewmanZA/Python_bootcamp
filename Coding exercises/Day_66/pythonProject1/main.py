# Import needed modules
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

# Initiate flask instance
app = Flask(__name__)


# Create database
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


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


# Define home page
@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read record(s)
@app.route("/random", methods=["GET"])
def get_random_cafe():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all", methods=["GET"])
def get_all_cafes():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    all_cafes = []
    for cafe in cafes:
        new_cafe = cafe.to_dict()
        all_cafes.append(new_cafe)
    return jsonify(cafes=all_cafes)


@app.route("/search", methods=["GET"])
def search_for_cafe():
    location = request.args.get("loc")
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    relevant_cafes = []
    for cafe in cafes:
        if cafe.location.upper() == location.upper():
            new_cafe = cafe.to_dict()
            relevant_cafes.append(new_cafe)

    if relevant_cafes:
        return jsonify(cafes=relevant_cafes)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


# HTTP POST - Create record
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."}), 200


# HTTP PUT/PATCH - Update record
@app.route("/update-price/<cafe_id>", methods=["GET", "PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    selected_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if selected_cafe:
        selected_cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


# HTTP DELETE - Delete record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        selected_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        if selected_cafe:
            db.session.delete(selected_cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
