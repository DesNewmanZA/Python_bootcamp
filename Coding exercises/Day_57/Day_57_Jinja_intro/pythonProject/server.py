# Import needed modules
from flask import Flask, render_template
from datetime import datetime

# Define global constants
CURRENT_YEAR = datetime.now().year

# Initiate flask instance
app = Flask(__name__)


# Define a home page
@app.route("/")
def home():
    return render_template("index.html", curr_yr=CURRENT_YEAR)


# Run site
if __name__ == "__main__":
    app.run(debug=True)
