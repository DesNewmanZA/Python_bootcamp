# The computer needs to randomly play
import random

# Assign ASCII representations of rock, paper, scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

imgs = [rock, paper, scissors]

# Input user choice
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# If input not rock/paper/scissors, default to losing
if my_choice not in [0, 1, 2]:
  print("Invalid choice - you lose!")
# Else, play the game
else:
    # Print out user choice
    print(imgs[my_choice])

    # Make computer choice
    pc_choice = random.randint(0,2)
    # Print out computer choice
    print("Computer chose:")
    print(imgs[pc_choice])

    # If I picked rock
    if my_choice == 0:
    # If computer picked scissors
        if pc_choice == 2:
            print("Rock beats scissors. You win!")
        # If computer picks paper
        elif pc_choice == 1:
            print("Paper beats rock. You lose!")
        # If computer picks rock
        else:
            print("Draw!")

    # If I picked paper
    elif my_choice == 1:
    # If computer picked scissors
        if pc_choice == 2:
            print("Scissors beats paper. You lose!")
        # If computer picked paper
        elif pc_choice == 1:
            print("Draw!")
        # If computer picked rock
        else:
            print("Paper beats rock. You win!")

    # If I picked scissors
    else:
        # If computer picked scissors
        if pc_choice == 2:
            print("Draw!")
        # If computer picked paper
        elif pc_choice == 1:
            print("Scissors beats paper. You win!")
        # If computer picked rock
        else:
            print("Rock beats scissors. You lose!")