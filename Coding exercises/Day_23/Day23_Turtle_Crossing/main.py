# Import needed modules
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialize game
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

# Take in user inputs
screen.listen()
screen.onkey(player.move_fwd, 'w')

# Start gameplay
game_is_on = True
while game_is_on:
    time.sleep(cars.car_speed)
    screen.update()
    cars.move_cars()

    # Test if turtle has reached the top
    if player.ycor() >= 280:
        scoreboard.update_score()
        player.reset_turtle()
        cars.car_speed *= 0.9

    # Detect collision with car
    for car in cars.car_list:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
