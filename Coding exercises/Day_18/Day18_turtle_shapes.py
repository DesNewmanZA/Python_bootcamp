# Import needed modules
from turtle import Turtle, Screen, colormode
from random import randint as ri

# Method to draw a shape
def draw_shape(corner_count):
    angle = 360 / corner_count
    for _ in range(corner_count):
        timmy.forward(100)
        timmy.left(angle)

# Initialize the turtle
timmy = Turtle()
timmy.shape('turtle')
timmy.color('chartreuse')

# Draw the shape in random colours
colormode(255)
for _ in range(3, 11):
    timmy.pencolor((ri(0, 255), ri(0, 255), ri(0, 255)))
    draw_shape(_)

screen = Screen()
screen.exitonclick()