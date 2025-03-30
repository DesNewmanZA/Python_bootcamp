# Get a string of student scores as input, split into a list 
student_scores = input().split()
# Convert each score into an integer
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Start a max score variable - minimum score is 0 so start there
max_score = 0 
# Check each possible score
for score in student_scores:
  # If the score is greater than the current max score, set to max score
  if score > max_score:
    max_score = score

# Print output
print(f"The highest score in the class is: {max_score}")