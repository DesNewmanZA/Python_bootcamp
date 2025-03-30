# Import needed modules
from turtle import Turtle, Screen, colormode
from random import randint as ri
from random import choice

# Initialize the turtle
timmy = Turtle()
timmy.shape('turtle')
timmy.color('chartreuse')
timmy.pensize(2)
timmy.speed('fastest')

# Draw the spirograph in random colours
colormode(255)
circle_num = ri(1,50)
tilt = int(360 / circle_num)
for _ in range(0, 360, tilt):
    timmy.pencolor((ri(0, 255), ri(0, 255), ri(0, 255)))
    timmy.circle(100)
    timmy.left(tilt)

screen = Screen()
screen.exitonclick()