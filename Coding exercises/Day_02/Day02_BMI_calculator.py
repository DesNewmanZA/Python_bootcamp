# Take in height and weight as inputs - assumed that the user has inputted accurately
height = input()
weight = input()

# Calculate BMI ensuring that the inputs are in the correct type format
BMI = int(weight)/float(height)**2
# Output BMI as a whole number
print(int(BMI))