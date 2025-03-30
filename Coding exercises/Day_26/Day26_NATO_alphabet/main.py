# Import needed modules
import pandas as pd

# Import the NATO alphabet data
NATO_alphabet = pd.read_csv('nato_phonetic_alphabet.csv')

# Convert the NATO alphabet into a dictionary
NATO_dict = {row.letter:row.code for (index, row) in NATO_alphabet.iterrows()}

# Take in a user's word that they would like to convert
word = input("Please input the word you would like to convert to a NATO alphabet: ").upper()

# Create the NATO alphabet version of the word and output the result
result = [NATO_dict[letter] for letter in [letter for letter in word]]
print(result)
