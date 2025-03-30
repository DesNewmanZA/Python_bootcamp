# Import module for ceiling function
import math

# Define a function that calculates the number of paint cans needed
def paint_calc(height, width, cover):
  number_of_cans = (height * width) / cover
  print(f"You'll need {math.ceil(number_of_cans)} cans of paint.")

# Take in user inputs in meters - assume inputs are the right format
test_h = int(input())
test_w = int(input()) 
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)