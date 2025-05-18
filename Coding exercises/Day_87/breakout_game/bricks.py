# Import needed modules
from turtle import Turtle


# Create brick class
class Brick(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=3, stretch_len=5)
        self.penup()
        self.goto(position)

    def destroy(self):
        self.goto(5000, 5000)