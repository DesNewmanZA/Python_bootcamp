# Import needed modules
from turtle import Turtle


# Create a scoreboard class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 250)
        self.write(self.l_score, align='center', font=('Courier', 30, "normal"))
        self.goto(100, 250)
        self.write(self.r_score, align='center', font=('Courier', 30, "normal"))

    def update_left_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def update_right_score(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align='center', font=('Courier', 30, "normal"))
        self.goto(100, 250)
        self.write(self.r_score, align='center', font=('Courier', 30, "normal"))
