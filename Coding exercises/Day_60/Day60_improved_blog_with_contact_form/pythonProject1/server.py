# Import needed modules
from flask import Flask, render_template, request
import requests
import smtplib

# Define global constants
EMAIL_ADDRESS = "MyEmail"
EMAIL_PASSWORD = "MyPassword"

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
@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", form_filled=True)
    return render_template("contact.html", form_filled=False)

# Define contact page
@app.route('/post/<int:num_id>')
def post(num_id):
    the_post = posts[int(num_id)-1]
    return render_template("post.html", the_post=the_post)

def send_email(name, email, phone, message):
    email_msg = f"Subject:Website contact request\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        connection.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, email_msg)


# Run development server
if __name__ == "__main__":
    app.run(debug=True)
