from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('chartreuse')

# Draw a dashed line
for _ in range(15):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)

screen = Screen()
screen.exitonclick()