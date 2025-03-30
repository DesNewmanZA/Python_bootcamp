# Import needed modules
from turtle import Turtle
import random


# Make a food class inheriting from turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        self.goto(random.randint(-280, 280), random.randint(-280, 260))

    # Method to make a new piece of food appear when the existing piece has been eaten
    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 260))
