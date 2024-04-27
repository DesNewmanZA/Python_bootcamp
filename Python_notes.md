# Python bootcamp - notes and syntax summary

## Strings
Strings need to be enclosed by quotes to be properly recognised.

    print("This is a valid string.")

You can use quotes in your string too, with some extra adjustments:

    print("A 'single quote' inside a double quote will work.")
    print('A "double quote" inside a single quote works too.')
    print("You can use \" and \" as well.")

You can add spaces to your text with "\n":

    print("An example of using line breaks:")
    print("\nHello world \nHello world \nHello world")

To concatentate strings, you can use a plus. Consider spacing needs when doing so!

    print("\nHello"+" "+"Des")

## Inputs
The function input("your text here") can be used to prompt for input. Note that you can nest functions within one another, such as this input function within a print statement.

    print("Hello "+input("What is your name? ")+"!")

# Variables
Variables are assigned with an equals sign. This allows us to store values for later referencing and use.

    name = input("What is your name? ")
    print(name)

When naming variables, ensure that they are easily readable. Spaces are not allowed, but an underscore is typically used in their place. Variable names are case sensitive. 

# Built-in functions
You can get the number of characters in a string using len('your string').

    length = len(name)
    print(length)