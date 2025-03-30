# Import needed modules
import pandas as pd

# Import the NATO alphabet data
NATO_alphabet = pd.read_csv('nato_phonetic_alphabet.csv')

# Convert the NATO alphabet into a dictionary
NATO_dict = {row.letter: row.code for (index, row) in NATO_alphabet.iterrows()}


# Take in a user's word that they would like to convert - handle for errors
def generate_alphabet():
    word = input("Please input the word you would like to convert to a NATO alphabet: ").upper()
    try:
        result = [NATO_dict[letter] for letter in [letter for letter in word]]
    except KeyError:
        print("Invalid input. Please input text with only letters from the alphabet.")
        generate_alphabet()
    else:
        print(result)


# Call function that converts text into NATO alphabet
generate_alphabet()
