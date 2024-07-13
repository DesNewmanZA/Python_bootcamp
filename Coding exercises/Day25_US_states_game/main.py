# Import needed modules
import pandas as pd
import turtle

# Initialize a screen
screen = turtle.Screen()
screen.title("US States guessing game")

# Make the screen the image of the blank states
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Import data of US states to use in the game
US_data = pd.read_csv('50_states.csv')

# Initialize score of correctly guessed states and set of correctly guessed states
score = 0
states_to_learn = set(US_data.state.to_list())

# While all states aren't guess
turtle_list = []
while score < 50:
    # Prompt for an answer
    answer_state = screen.textinput(title=f'{score}/50 states guessed', prompt='What is another state name?').title()
    # Test to see if the user inputted a correct state
    needed_row = US_data[US_data.state == answer_state]
    # If inputted exit, exit the loop
    if answer_state == "Exit":
        break
    # If correct, write to screen using a turtle, discard guess from states to learn and add one to score
    if len(needed_row) > 0:
        score += 1
        states_to_learn.discard(answer_state)
        x_cor = needed_row['x'].iloc[0]
        y_cor = needed_row['y'].iloc[0]
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(x_cor, y_cor)
        new_turtle.write(answer_state, move=False, align='left', font=('Arial', 8, 'normal'))

# At end of game, output the states needed to learn
states_to_learn = pd.DataFrame(states_to_learn)
states_to_learn.to_csv('states_to_learn.csv')
