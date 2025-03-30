# Import needed modules
from turtle import Turtle, Screen

# Initialize turtle and screen
tim = Turtle()
screen = Screen()

# Define function that moves turtle 10 paces
def move_fwd():
    tim.forward(10)

# Listens for an event
screen.listen()
# Waits for spacebar to execute move forward 
# Note: passing function as an argument - no brackets!
screen.onkey(key='space', fun=move_fwd)
screen.exitonclick()