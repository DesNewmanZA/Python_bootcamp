# Import needed modules
from flask import Flask, render_template
import requests

# Start flask instance
app = Flask(__name__)

# Get sample blog content
response = requests.get(url="https://api.npoint.io/3de1b2f68ad27bd660ae")
posts = response.json()

# Initiate home page
@app.route('/')
def home():
    return render_template("index.html", posts=posts)

# Define about page
@app.route('/about')
def about():
    return render_template("about.html")

# Define contact page
@app.route('/contact')
def contact():
    return render_template("contact.html")

# Define contact page
@app.route('/post/<int:num_id>')
def post(num_id):
    the_post = posts[int(num_id)-1]
    return render_template("post.html", the_post=the_post)



# Run development server
if __name__ == "__main__":
    app.run(debug=True)
