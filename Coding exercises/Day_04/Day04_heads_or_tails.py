# Coin flipping simulations require randomness
import random

# Pull a random integer that takes on the values 0 or 1
random_num = random.randint(0,1)

# If the integer is 1, it is Heads. Else, Tails.
if random_num == 1:
  print("Heads")
else:
  print("Tails")