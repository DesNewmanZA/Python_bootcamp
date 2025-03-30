print("Welcome to the tip calculator.")
# Take in total bill - consider decimals!
bill = float(input("What was the total bill? R"))
# Take in the tip percentage - assume a round number. 
# Removed imposed bounds on initial problem to be more general
tip = int(input("What percentage tip would you like to give? "))
# Take in the number of people to split the bill by - assume an integer
num_people = int(input("How many people to split the bill? "))

# Calculate the bill with tip included
bill_with_tip = bill * (1 + tip / 100)
# Calculate the bill with tip per person - format to look like currency
tipped_bill_per_person = "{:.2f}".format(bill_with_tip/num_people)
# Output the answer
print(f"Each person should pay: R{tipped_bill_per_person}.")