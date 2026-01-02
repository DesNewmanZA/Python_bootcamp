# Import needed modules
import turtle


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.penup()
        self.setposition(-370, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="left",
                   font=("Arial", 14, "normal"))

    def add_point(self, points=10):
        self.score += points
        self.update_score()
