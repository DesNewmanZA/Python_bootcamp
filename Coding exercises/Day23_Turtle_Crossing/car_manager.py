# Import needed modules
from turtle import Turtle
import random

# Define constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUM_CARS = 30
START_SPEED = 0.15


# Define car manager class
class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed = START_SPEED
        for _ in range(NUM_CARS):
            self.make_car()

    # Move the car - if off-screen enough, restart position
    def move_cars(self):
        for _ in range(NUM_CARS):
            self.car_list[_].goto(self.car_list[_].xcor()-MOVE_INCREMENT, self.car_list[_].ycor())
            if self.car_list[_].xcor() < -350:
                self.car_list[_].goto(300, random.randint(-240, 270))

    def make_car(self):
        temp_car = Turtle()
        temp_car.color(random.choice(COLORS))
        temp_car.shapesize(stretch_wid=1, stretch_len=2)
        temp_car.shape('square')
        temp_car.penup()
        temp_car.goto(random.randint(300, 900), random.randint(-240, 270))
        self.car_list.append(temp_car)
