# Import needed packages
from flask import Flask, render_template

# Create flask instance
app = Flask(__name__)

# Define home page
@app.route('/')
def home():
    return render_template('index.html')


# Call up the website
if __name__ == "__main__":
    app.run(debug=True)