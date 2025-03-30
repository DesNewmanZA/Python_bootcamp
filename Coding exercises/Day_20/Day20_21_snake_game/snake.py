# Import needed modules
from turtle import Turtle

# Initialize constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_STARTING_SIZE = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Make a snake class that controls the snake's display, movements and growth
class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    # Create a snake body out of turtles - note that turtles are 20 x 20 pixels
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Create a method that adds a new segment onto the snake as required
    def add_segment(self, position):
        temp_turtle = Turtle(shape='square')
        temp_turtle.color('white')
        temp_turtle.penup()
        temp_turtle.goto(position)
        self.snake_segments.append(temp_turtle)

    # Create a method to add a segment onto the end of the snake
    def extend_snake(self):
        self.add_segment(self.snake_segments[-1].position())

    # Method to move snake by shifting up into prior segment's position
    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            xpos_ahead = self.snake_segments[seg_num - 1].xcor()
            ypos_ahead = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(xpos_ahead, ypos_ahead)
        # Head must move forward - all other segments follow its lead
        self.head.forward(20)

    # Methods to respond to the directions provide by the user
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
