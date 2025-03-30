# Import needed modules
from turtle import Turtle, Screen

# Initialize turtle and screen
tim = Turtle()
screen = Screen()

# Define functions that define movement for the turtle
def move_fwd():
    tim.forward(10)

def move_bwd():
    tim.forward(-10)

def move_ccw():
    tim.setheading(tim.heading()+10)

def move_cw():
    tim.setheading(tim.heading()-10)

def reset_screen():
    screen.resetscreen()

# Listens for an event
screen.listen()
# Waits for spacebar to execute move forward 
# Note: passing function as an argument - no brackets!
screen.onkey(key='w', fun=move_fwd)
screen.onkey(key='s', fun=move_bwd)
screen.onkey(key='d', fun=move_cw)
screen.onkey(key='a', fun=move_ccw)
screen.onkey(key='c', fun=reset_screen)

# Exit only when screen clicked on
screen.exitonclick()