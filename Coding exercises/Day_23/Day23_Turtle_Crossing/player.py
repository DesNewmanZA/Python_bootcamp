# Import needed modules
from turtle import Turtle

# Define constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# Define player class
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.tilt(90)
        self.goto(STARTING_POSITION)

    def move_fwd(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def reset_turtle(self):
        self.goto(STARTING_POSITION)
