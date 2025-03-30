# Ask user for height, assumption made that input is of a numeric type, converted to a float
height = float(input())
# Ask user for weight, assumption made that input is of a numeric type, converted to a integer
weight = int(input())
# Calculate BMI
BMI = weight / height ** 2

# Classify BMI according to medical terms
if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly overweight.") 
elif BMI < 35:
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print(f"Your BMI is {BMI}, you are clinically obese.")
