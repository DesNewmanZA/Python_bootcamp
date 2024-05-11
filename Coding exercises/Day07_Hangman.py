# Import needed modules
import random
import Day07_Hangman_art
import Day07_Hangman_words

print(Day07_Hangman_art.logo)

# Create a boolean variable to control whether the game is over or not
end_of_game = False

# The below word list is assumed
word_list = Day07_Hangman_words.word_list

# Pick a word from the word list at random
chosen_word = random.choice(word_list)

# Create blanks list with length equalling chosen word
display = ["_" for letter in chosen_word]

# Start out with 6 lives
lives = 6

while end_of_game == False:
    # Take a guessed letter from the user - assume input is correct type
    guess = input("Guess a letter: ").lower()

    # If letter already guessed, let user know
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check if the guessed letter is in the chosen word
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = chosen_word[i]

    print(f"{' '.join(display)}")

    # If guess isn't in the word, deduct a life
    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word. You lose a life!")
        print(f"You have {lives} lives left!")

    # Stop game if no lives left
    if lives == 0:
        end_of_game = True
        print("You lose!")

    # Check if all letters have been guessed
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(Day07_Hangman_art.stages[lives])