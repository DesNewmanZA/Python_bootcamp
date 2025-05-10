# Import needed modules
from translator import translator

# Define translation directions
TO_MORSE = "1"
TO_ALPHA = "2"
TO_QUIT = "3"


# Define a function to print out valid choices in the program
def print_options():
    """
    Prints out the options available to the user within the program

    Args: None

    Returns: None
    """
    print("Please select what you would like to do:")
    print("\t Type 1 for translating an alphanumeric message into Morse code")
    print("\t Type 2 for translating a Morse code message into alphanumeric")
    print("\t Type 3 to quit \n")


# Initialize translator
print("Welcome to the alphanumeric-Morse code translator!\n")
running = True

# While user wants to continue, prompt for valid input
while running:
    print_options()

    # Prompt user for a valid input
    user_input = ''
    while user_input not in ("1", "2", "3"):
        user_input = input("Please input your selection: ")

        if user_input == TO_MORSE:
            user_msg = input("Please input the message you would like to translate to Morse code: ")
            print(f"{translator(user_msg, user_input)}\n")
        elif user_input == TO_ALPHA:
            user_msg = input("Please input the message you would like to translate to alphanumeric: ")
            print(f"{translator(user_msg, user_input)}\n")
        elif user_input == TO_QUIT:
            print("\n Thank you for using the alphanumeric-Morse code translator! Goodbye!")
            running = False
        else:
            print("\n Invalid choice.\n")
            print_options()
