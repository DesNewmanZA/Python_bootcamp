# Take in an integer as input - assuming the data type inputted is accurate
number = int(input())

# Even numbers have no remainder when divided by two
if number % 2 == 0:
  print("This is an even number.")
# If the condition above fails, it means the number has to be odd
else:
  print("This is an odd number.")