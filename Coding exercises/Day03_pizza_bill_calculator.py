# Start the calculator with a hello message
print("Thank you for choosing Python Pizza Deliveries!")
# Take in the size as an input
size = input("What size pizza do you want? S, M or L ")
# Take in whether the customer wants pepperoni
add_pepperoni = input("Do you want pepperoni? Y or N ") 
# Take in whether the customer wants extra cheese
extra_cheese = input("Do you want extra cheese? Y or N ") 

# The bill starts out at 0. We will add to the bill as each item becomes available
bill = 0

# Calculation of price depending on size of pizza and extras
if size == "S":
  bill += 15
  if add_pepperoni == "Y":
    bill += 2
    if extra_cheese == "Y":
      bill += 1
  else:
    if extra_cheese == "Y":
      bill += 1
elif size == "M":
  bill += 20
  if add_pepperoni == "Y":
    bill += 3
    if extra_cheese == "Y":
      bill += 1
  else:
    if extra_cheese == "Y":
      bill += 1
else:
  bill += 25
  if add_pepperoni == "Y":
    bill += 3
    if extra_cheese == "Y":
      bill += 1
  else:
    if extra_cheese == "Y":
      bill += 1

# Output the final bill
print(f"Your final bill is: ${bill}.")