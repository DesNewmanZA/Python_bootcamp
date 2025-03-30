# Import needed modules
from flask import Flask, render_template
import requests

# Start flask instance
app = Flask(__name__)

# Define home page
@app.route('/')
def home():
    posts = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", posts=posts)

# Define post pages
@app.route('/post/<int:num_id>')
def get_post(num_id):
    posts = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
    selected_post = posts[num_id-1]
    return render_template("post.html", post=selected_post)

# Run instance of website
if __name__ == "__main__":
    app.run(debug=True)
