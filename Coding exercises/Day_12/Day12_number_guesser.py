# Import needed modules
import random

# Initialize game with a welcome statement
print("Welcome to the Number Guessing game!")
print("I'm thinking of a number between 1 and 100.")

# Get the user to input a difficulty level
difficulty = ''
while difficulty not in ('easy', 'hard'):
    difficulty = input("Choose a difficulty - type 'easy' or 'hard': ").lower()

# Set number of lives based on the difficulty
if difficulty == 'easy':
    lives = 10
else:
    lives = 5

# Generate the number the computer is thinking of
random_int = random.randint(1, 100)

# Allow user to guess a number while lives > 0
while lives > 0:
    # Take in a guess
    print(f"You have {lives} attempts remaining.")
    guess = int(input("Make a guess: "))

    # Determine if too high, too low or correct
    if guess == random_int:
        print(f"You got it! The answer is {random_int}")
        lives = 0
    elif guess > random_int:
        print("Too high!")
    else:
        print("Too low!")

    # Remove a life for each wrong guess
    lives -= 1

    # Print answer if the user has run out of lives
    if lives == 0:
        print(f"You lose! The number was {random_int}.")

    # Denote each turn by a line
    print('_______________________')