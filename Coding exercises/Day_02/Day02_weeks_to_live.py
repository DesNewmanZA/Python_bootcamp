# Get user's age as input. Assuming input is correct
age = input()
# Assume living until 90 and there are 52 weeks in a year
# Convert age to an integer and calculate number of weeks left
num_weeks_left = (90-int(age))*52
# Output result
print(f"You have {num_weeks_left} weeks left.")