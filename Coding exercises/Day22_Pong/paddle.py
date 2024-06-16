# Import needed modules
from turtle import Turtle

# Initialize constants
Y_POS = 0
STEP_SIZE = 20


# Create a paddle class
class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto((x_pos, Y_POS))

    def up(self):
        if self.ycor() <= 300 - STEP_SIZE * 4:
            new_y = self.ycor() + STEP_SIZE
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() >= -300 + STEP_SIZE*4:
            new_y = self.ycor() - STEP_SIZE
            self.goto(self.xcor(), new_y)
