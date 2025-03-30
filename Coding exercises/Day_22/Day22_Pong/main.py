# Import needed modules
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Define constants
SPEED_INCR = 0.9

# Create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

# Create paddles, ball, scoreboard
r_paddle = Paddle(380)
l_paddle = Paddle(-380)
ball = Ball()
scoreboard = Scoreboard()

# Listen for user input and move snake accordingly
screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

# Play game while game is still active
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if (ball.xcor() > 350 and ball.distance(r_paddle) < 50) or (ball.xcor() < -350 and ball.distance(l_paddle) < 50):
        ball.bounce_x()
        ball.move_speed *= SPEED_INCR

    # Detect if right paddle scores a point
    elif ball.xcor() < - 370:
        ball.reset_position()
        scoreboard.update_right_score()

    # Detect if left paddles scores a point
    elif ball.xcor() > 370:
        ball.reset_position()
        scoreboard.update_left_score()

screen.exitonclick()
