# Import needed modules
from flask import Flask, render_template, request

# Make a flask instance
app = Flask(__name__)

# Make a home page
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
    return render_template("login.html", name=name, pwd=password)

# Run instance
if __name__ == "__main__":
    app.run(debug=True)