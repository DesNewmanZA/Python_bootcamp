# Import needed module
import random

# Define reference list of letters, numbers and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Initialize generator and ask user for inputs
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Make an empty list to hold characters for the password
pwd_list = []

# Generate and append random symbols, numbers and letters
for symbol in range(0, nr_symbols):
    pwd_list.append(random.choice(symbols))

for number in range(0, nr_numbers):
    pwd_list.append(random.choice(numbers))

for letter in range(0, nr_letters):
    pwd_list.append(random.choice(letters))

# Shuffle the selected characters
random.shuffle(pwd_list)

# Return generated passwords
print(f"Your password is {''.join(pwd_list)}")