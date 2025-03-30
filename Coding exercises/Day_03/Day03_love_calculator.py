# Take in two names to calculate the love score
name1 = input('What is your name? ') 
name2 = input('What is their name? ') 
print("The Love Calculator is calculating your score...")

# Ensure the names are in lower case for counting correctly and combine
both_names = (name1+name2).lower()
# Define the two comparative strings
true = 'true'
love = 'love'

# Calculate a score for letters in 'true'
score_true = 0
for letter in true:
  score_true += both_names.count(letter)

# Calculate a score for letters in 'love'
score_love = 0
for letter in love:
  score_love += both_names.count(letter)

# Calculate a final score by combining the digits
final_score = int(str(score_true)+str(score_love))

# Output the final love score and according message
if final_score < 10 or final_score > 90:
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif 40 < final_score and final_score < 50:
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is {final_score}.")