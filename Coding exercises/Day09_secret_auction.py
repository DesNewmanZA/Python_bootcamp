# Define clearing function
import os
clear = lambda: os.system('cls')
# Define logo art
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# Initialize, starting with the logo
print(logo)

# Make a dictionary to store bids per person
bids = {}

# Make a while loop that continues while continue is True
redo = "yes"
while redo == "yes":
    name = input("What is your name?: ")
    price = int(input("What is your bid price? R"))
    bids[name] = price

    redo = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if redo == "yes":
        clear()

# Find highest bid
max_bid = 0
winner = ''
for name in bids:
    if bids[name] > max_bid:
        max_bid = bids[name]
        winner = name
        
# Print the winner
print(f"The winner is {winner} with a bid of R{max_bid}.")