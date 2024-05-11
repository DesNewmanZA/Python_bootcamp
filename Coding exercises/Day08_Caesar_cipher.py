# Define the alphabet
alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z'
            ]

# Define the caesar function
def caesar(text, shift, direction):
  # Initialize the adjusted message
  adj_text = ""
  # If decoding, the shift is backwards
  if direction == "decode":
    shift *= -1

  # For each letter in the text
  for letter in text:
    # Get the adjusted letter index
    new_index = (alphabet.index(letter) + shift) % len(alphabet)
    # Update the adjusted message
    adj_text = adj_text + alphabet[new_index]
  # Output the adjusted message
  print(f"The {direction}d text is {adj_text}.")

# Repeat while user wants to continue
repeat = True
while repeat:
    # Define the inputs - direction, text to use and shift
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    repeat_test = input(
        "Would you like to go again? Type 'yes' or 'no'.\n").lower()
    if repeat_test == 'no':
        repeat = False
