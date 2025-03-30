# Import needed modules
import colorgram
from turtle import Turtle, Screen, colormode
from random import choice


# Method to draw a dot
def draw_dot():
    timmy.pendown()
    timmy.pencolor(choice(palette))
    timmy.dot(30)
    timmy.penup()


# Extract colours from the reference image and make a colour palette
colours = colorgram.extract('Hirst.jpg', 30)
palette = []
for colour in colours:
    rgb = colour.rgb
    if rgb.r <= 230 and rgb.g <= 230 and rgb.b <= 230:
        palette.append((rgb.r, rgb.g, rgb.b))

# Initialize screen
screen = Screen()
screen.screensize(400, 400)
colormode(255)

# Initialize the turtle
timmy = Turtle(visible=False)
timmy.speed('fastest')
timmy.penup()
timmy.goto(-310, -270)

# Perform painting
for dot_count in range(1, 12*8):
    if dot_count % 8 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(800)
        timmy.setheading(0)

    draw_dot()
    timmy.forward(100)

# Show outputs
screen.exitonclick()
