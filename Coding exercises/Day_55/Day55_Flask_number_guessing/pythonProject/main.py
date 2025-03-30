# Import needed modules
from flask import Flask
import random

# Generate random number
RANDOM_NUMBER = random.randint(0, 9)
COLOUR_LIST = ['aquamarine', 'aqua', 'blue', 'chartreuse', 'coral', 'crimson', 'darkorchid', 'green', 'orange',
               'yellow']

# Initialize flask instance
app = Flask(__name__)


# Define paths and respective views
@app.route("/")
def home():
    return ("<h1>Guess a number between 0 and 9 </h1> <img src = "
            "'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")


@app.route('/<int:number>')
def number_guess(number):
    guess_colour = COLOUR_LIST[number]
    if number < RANDOM_NUMBER:
        return (f"<h1 style = 'color: {guess_colour}'>Too low, try again!</h1> <img src = "
                f"'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")
    elif number > RANDOM_NUMBER:
        return (f"<h1 style = 'color: {guess_colour}'>Too high, try again!</h1> <img src = "
                f"'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")
    else:
        return (f"<h1 style = 'color: {guess_colour}'>You found me!</h1> <img src = "
                f"'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")


# Run this instance in debug mode
if __name__ == '__main__':
    app.run(debug=True)
