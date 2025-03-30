# Import needed modules
from turtle import Turtle

# Initialize constants
X_MOVE = 10
Y_MOVE = 10
STARTING_SPEED = 0.05


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.shape('circle')
        self.penup()
        self.x_move = X_MOVE
        self.y_move = Y_MOVE
        self.move_speed = STARTING_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x, new_y))

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = STARTING_SPEED
