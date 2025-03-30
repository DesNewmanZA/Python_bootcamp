# Import needed modules
from flask import Flask, render_template
from datetime import datetime
import requests

# Define global constants
CURRENT_YEAR = datetime.now().year

# Initiate flask instance
app = Flask(__name__)


# Define a home page
@app.route("/")
def home():
    return render_template("index.html", curr_yr=CURRENT_YEAR)


@app.route("/<string:name_var>")
def guess(name_var):
    gender = requests.get(url=f'https://api.genderize.io?name={name_var}').json()['gender']
    age = requests.get(url=f'https://api.agify.io?name={name_var}').json()['age']
    return render_template("guess.html", gender=gender, age=age, name=name_var.title())

@app.route("/blog")
def get_blog():
    posts = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", posts=posts)

# Run site
if __name__ == "__main__":
    app.run(debug=True)
