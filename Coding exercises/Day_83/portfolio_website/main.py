# Import needed modules
from flask import Flask, render_template
import json

# Make a Flask instance
app = Flask(__name__)


# Define a home page
@app.route("/")
def home():
    with open('content/about.txt') as f:
        about_text = f.read()
    with open('content/awards.json') as f:
        awards_data = json.load(f)
    with open('content/education.json') as f:
        edu_data = json.load(f)
    with open('content/interests.json') as f:
        interest_data = json.load(f)
    with open('content/languages.json') as f:
        language_data = json.load(f)
    with open('content/expertise_areas.json') as f:
        expert_data = json.load(f)
    with open('content/experience.json') as f:
        experience_data = json.load(f)
    return render_template("index.html", about_text=about_text, awards=awards_data,
                           education=edu_data, interests=interest_data, languages=language_data,
                           expertise=expert_data, experience_hist=experience_data)


# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
