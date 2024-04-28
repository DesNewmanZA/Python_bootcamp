# Who pays is selected randomly
import random

# Take in a list of names separated by ", " - assumption that input is correct
names = names_string.split(", ")

# Calculate number of options of people paying
num_names = len(names)-1
# Create a random integer in the range of options
rand_int = random.randint(0,num_names)
# Use random integer to select who pays today
print(f"{names[rand_int]} is going to buy the meal today!")