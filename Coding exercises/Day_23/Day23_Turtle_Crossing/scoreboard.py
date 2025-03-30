# Import needed modules
from turtle import Turtle

# Define constants
FONT = ("Courier", 24, "normal")


# Define scoreboard class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(-250, 280)
        self.level = 1
        self.update_scoreboard()

    # Method to update the presented scoreboard
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level = {self.level}", False, align="center", font=("Courier", 12, "normal"))

    def update_score(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", False, align="center", font=("Courier", 12, "normal"))
