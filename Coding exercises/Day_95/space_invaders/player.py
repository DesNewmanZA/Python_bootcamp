# Import needed modules
import turtle


# Define player class
class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.color('blue')
        self.penup()
        self.speed(0)
        self.setposition(0, -250)
        self.setheading(90)
        self.player_speed = 15

    def move_left(self):
        x = self.xcor()
        x -= self.player_speed
        if x < -340:
            x = -340
        self.setx(x)

    def move_right(self):
        x = self.xcor()
        x += self.player_speed
        if x > 340:
            x = 340
        self.setx(x)
