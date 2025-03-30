# Import needed modules
from flask import Flask, render_template

# Create an instance of flask
app = Flask(__name__)

# Create home page
@app.route("/")
def home():
    return render_template('index.html')

# Run server
if __name__ == "__main__":
    app.run(debug=True)