# Import needed modules
from turtle import Turtle

# Initialize constants
Y_POS = -250
STEP_SIZE = 20


# Create a paddle class
class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.penup()
        self.goto((x_pos, Y_POS))

    def right(self):
        if self.xcor() <= 400 - STEP_SIZE * 4:
            new_x = self.xcor() + STEP_SIZE
            self.goto(new_x, self.ycor())

    def left(self):
        if self.xcor() >= -400 + STEP_SIZE*4:
            new_x = self.xcor() - STEP_SIZE
            self.goto(new_x, self.ycor())
