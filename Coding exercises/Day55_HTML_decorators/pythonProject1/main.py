# Import needed modules
from flask import Flask

# Initialize flask instance
app = Flask(__name__)

# Define decorators
def make_bold(fx):
    def wrapper():
        return f"<b> {fx()} </b>"
    return wrapper

def make_emphasized(fx):
    def wrapper():
        return f"<em> {fx()} </em>"
    return wrapper

def make_underlined(fx):
    def wrapper():
        return f"<u> {fx()} </u>"
    return wrapper


# Define paths and respective views
@app.route("/")
@make_bold
@make_underlined
@make_emphasized
def hello_world():
    return "<h1 style='text-align: center'>Hello world</h1>"


@app.route('/bye')
def goodbye():
    return "Goodbye!"


@app.route('/<name>')
def specific_greeting(name):
    return f"Hi {name}!"


# Run this instance in debug mode
if __name__ == '__main__':
    app.run(debug=True)
