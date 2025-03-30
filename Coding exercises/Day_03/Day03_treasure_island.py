# Print an old-school ASCII title
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First choice - crossroad
choice = input(
    "You are at a crossroad. Where do you want to go? Type 'left' or 'right'\n"
).lower()

if choice != "left":
    print("You fell into a hole! Game over")
else:
    # Second choice - island within a lake
    print("You\'ve come to a lake! In the middle, there is an island.\n")
    choice = input(
        "Do you wait for a boat or try swim to the island?\n").lower()
    if choice != "wait":
        print("You were attacked by a trout! Game over")
    else:
        # Third choice - which door to pick?
        print("You took a boat.\n")
        print(
            "You arive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue\n"
        )
        choice = input("Which door do you choose?\n").lower()
        if choice == "red":
            print("You got burned by fire! Game over!")
        elif choice == "blue":
            print("You were eaten by beasts! Game over!")
        elif choice != "yellow":
            print("Game over!")
        else:
            print("You found the treasure! You win!")
