# Import needed modules
from turtle import Turtle, Screen, TK
import random

# Initialize screen
screen = Screen()
screen.setup(width=500, height=400)

# Initialize colour list
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# Prompt user for which turtle they believe will win
bet = screen.textinput(title="Make your bet!", 
                 prompt="Which turtle will win the race? Enter a colour: ").lower()

# Initialize turtles
turtles = []
start_incr = 100
for colour in colours:
    temp_turtle = Turtle(shape='turtle')
    temp_turtle.color(colour)
    temp_turtle.penup()
    temp_turtle.goto(x=-230, y=start_incr)
    turtles.append(temp_turtle)
    start_incr = start_incr - 30

# Race the turtles
is_race_on = True
while is_race_on:
    for turtle in turtles:
        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)
        # Check if there's a winner and output the outcome
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == bet:
                TK.messagebox.showinfo(title="Race outcome", message=f"You won! The {winner} turtle came first")
            else:
                TK.messagebox.showinfo(title="Race outcome", message=f"You lose! The {winner} turtle came first")

# Exit only when screen clicked on
screen.exitonclick()