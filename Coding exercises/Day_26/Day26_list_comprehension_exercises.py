###################
# SQUARED NUMBERS #
###################

# Initialize list of numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# Use list comprehension to square the numbers in a single line of code
squared_numbers = [number ** 2 for number in numbers]

# Output results
print(squared_numbers)


################
# EVEN NUMBERS #
################

# Initialize string of numbers
list_of_strings = '1, 1, 2, 3, 5, 8, 13, 21, 34, 55'.split(',')

# Convert list of strings into integers
list_of_ints = [int(num) for num in list_of_strings]

# Only keep the even numbers
result = [num for num in list_of_ints if num % 2 == 0]

# Output results
print(result)

#####################################
# DICTIONARY COMPREHENSION PRACTICE #
#####################################

# Import random module
import random

# Define names
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# Assign each student a random score
student_scores = {name: random.randint(0, 100) for name in names}

# Output only students that have passed
passed_students = {name:score for (name, score) in student_scores.items() if score > 50}
print(passed_students)