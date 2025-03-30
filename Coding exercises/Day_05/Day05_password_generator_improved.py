# Import needed module
import random
import string 

# Define reference list of letters, numbers and symbols
letters = list(string.ascii_lowercase + string.ascii_uppercase)
numbers = [str(i) for i in range(0, 10)]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] # Kept hardcoded as not all symbols are useful in a password

# Initialize generator and ask user for inputs - assumes inputs are correct format and numbers are sensible
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How long would you like your password to be?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Make an empty list to hold characters for the password
pwd_list = []

# Generate and append random symbols, numbers and letters
for symbol in range(0, nr_symbols):
    pwd_list.append(random.choice(symbols))

for number in range(0, nr_numbers):
    pwd_list.append(random.choice(numbers))

for letter in range(0, nr_letters - nr_symbols - nr_numbers):
    pwd_list.append(random.choice(letters))

# Shuffle the selected characters
random.shuffle(pwd_list)

# Return generated passwords
print(f"Your password is {''.join(pwd_list)}")