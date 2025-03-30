# Input a target number to sum up evens until
target = int(input()) 

# Create a variable to hold the total sum
total = 0
# Sum up each even number until the target is hit
for num in range(0, target + 1, 2):
  total += num

print(total)