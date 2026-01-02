import turtle


class Bullet(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.state = "ready"
        self.move_speed = 5

    def fire(self, x, y):
        if self.state == "ready":
            self.state = "fire"
            self.goto(x, y)
            self.showturtle()

    def move(self):
        if self.state == "fire":
            self.sety(self.ycor() + self.move_speed)
            if self.ycor() > 280:
                self.reset_bullet()

    def reset_bullet(self):
        self.hideturtle()
        self.state = "ready"
