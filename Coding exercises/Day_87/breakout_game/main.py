# Import needed modules
import time
import random
from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from bricks import Brick

# Create constants
BALL_COLOURS = ['blue', 'green', 'yellow', 'red', 'orange']

# Create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Breakout")
screen.tracer(0)

# Initialize set up
# I'm not adding too many brick rows else it is a bit tedious
ball = Ball()
paddle = Paddle(0)
bricks = []
for row in range(2):
    for col in range(6):
        brick = Brick((-300 + col * 120, 250 - row * 80), random.choice(BALL_COLOURS))
        bricks.append(brick)

# Listen for user input and move paddle accordingly
screen.listen()
screen.onkey(paddle.right, 'Right')
screen.onkey(paddle.left, 'Left')

# Play game while game is still active
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with bricks
    for brick in bricks:
        if (brick.xcor() - 55 < ball.xcor() < brick.xcor() + 55) and (brick.ycor() - 55 < ball.ycor() < brick.ycor() + 55):
            brick.destroy()
            bricks.remove(brick)
            ball.bounce_y()

    # Detect collision with wall
    if ball.xcor() >= 380 or ball.xcor() <= -380:
        ball.bounce_x()

    # Detect collision with paddle
    if (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50) and (paddle.ycor() - 25 < ball.ycor() < paddle.ycor() + 25):
        ball.bounce_y()

    # Detect collision with roof
    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect falling through fall
    if ball.ycor() < -280:
        ball.reset_position()

    # Test if game is over
    if len(bricks) == 0:
        screen.update()
        game_on = False
        win_msg = Turtle()
        win_msg.color("white")
        win_msg.hideturtle()
        win_msg.penup()
        win_msg.goto(0, 0)
        win_msg.write("You win!", font=("Arial", 40), align="center")

# Keep game running until clicked
screen.exitonclick()
