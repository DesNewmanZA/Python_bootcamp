# Input student heights in a single input, split apart into a list
student_heights = input().split()
# Convert the heights into integers
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# Initalize counters for the number of students and total heights
num_students = 0
total_height = 0
# For each student, add to the tallies
for student in student_heights:
  num_students += 1
  total_height += student

# Output results
print(f"total height = {total_height}")
print(f"number of students = {num_students}")
print(f"average height = {int(round(total_height/num_students,0))}")
