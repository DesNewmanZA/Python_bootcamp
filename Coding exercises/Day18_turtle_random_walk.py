# Import needed modules
from turtle import Turtle, Screen, colormode
from random import randint as ri
from random import choice

# Initialize the turtle
timmy = Turtle()
timmy.shape('turtle')
timmy.color('chartreuse')
timmy.pensize(10)
timmy.speed('fastest')

# Draw the random walk in random colours
colormode(255)
directions = [0, 90, 180, 270]
for _ in range(100):
    timmy.pencolor((ri(0, 255), ri(0, 255), ri(0, 255)))
    timmy.forward(30)
    timmy.setheading(choice(directions))

screen = Screen()
screen.exitonclick()