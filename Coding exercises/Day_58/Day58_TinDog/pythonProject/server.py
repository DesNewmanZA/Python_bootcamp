# Import needed modules
from flask import Flask, render_template

# Initiate flask instance
app = Flask(__name__)


# Initialize home page
@app.route('/')
def home():
    return render_template('index.html')


# Start server upon running script
if __name__ == "__main__":
    app.run(debug=True)
