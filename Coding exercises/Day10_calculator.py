# Define the 4 calculator functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Create a dictionary to store the functions according to symbol picked
operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

# Calculate only while the user still has more numbers to input
calc_on = True
# Ask for first number input
num1 = float(input("What's the first number?: "))
while calc_on:
    # Ask for operation
    for symbol in operations:
        print(symbol)
    op_text = input("Pick an operation: ")

    # Ask for subsequent number input
    num2 = float(input("What's the next number?: "))

    # Call the function according to the symbol picked
    ans = operations[op_text](num1, num2)

    # Ask the user if they want to continue
    cont = input(
        'Type "y" to continue calculating with {ans}, or type "n" to exit: '
    ).lower()
    if cont == 'n':
        calc_on = False

    # Store answer as num1 for next calculation
    num1 = ans

# Print the final answer
print(f"The final answer is {ans}.")
