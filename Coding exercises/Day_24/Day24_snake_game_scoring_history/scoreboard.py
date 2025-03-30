# Import needed modules
from turtle import Turtle


# Initialize scorecard class, inheriting from turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        with open('data.txt') as my_file:
            self.high_score = int(my_file.read())
        self.update_scoreboard()

    # Method to update the presented scoreboard
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}. High score: {self.high_score}", False, align="center", font=("Courier", 12, "normal"))

    # Method to update the score when a piece of food is eaten
    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    # Method to reset game and save score
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as my_file:
                my_file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()