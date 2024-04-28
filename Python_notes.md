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

We can select parts of a string using square brackets. Our counter always starts at 0.

    print("Hello"[0])
    H

You can also index negatively. To get the last element for example, we would use [-1].

    print("Hello"[-1])
    o

# Integers
These are simply whole numbers without decimals, and are inputted as plain numbers.

Note that you can't concatenate strings and integers without some conversion.

# Floats
These are numbers with decimals.
You can make large numbers more readable by adding an underscore.

    734_529.678

Note that you can't concatenate strings and floats without some conversion.

If we want our float to have a certain number of digits, we can use the format() function. The example below formats with 2 decimal places.

    "{:.2f}".format(my_num)

# Boolean
This is a binary variable, only holding the values True or False. Note the capitalisation.

## Inputs
The function input("your text here") can be used to prompt for input. Note that you can nest functions within one another, such as this input function within a print statement.

    print("Hello "+input("What is your name? ")+"!")

# Variables
Variables are assigned with an equals sign. This allows us to store values for later referencing and use.

    name = input("What is your name? ")
    print(name)

When naming variables, ensure that they are easily readable. Spaces are not allowed, but an underscore is typically used in their place. Variable names are case sensitive. 

# Built-in functions
You can get the number of characters in a string using len('your string'). It can't be used on numeric data types.

    length = len(name)
    print(length)

You can check variable types with type()

    type("Hello")
    str

# Type casting
Convert a variable to a string:

    str(my_var)

Convert a variable to a float:

    float(my_var)

Convert a variable to an integer:

    int(my_var)

Note that the above just chops off the floating point, no rounding takes place.

If you want to print different types together, we can use an f string.

    print(f"Your score is {score}")

# Mathematical operations
Addition is done with a +:

    print(3 + 2)
    5

Subtraction is done with a -:

    print(3-2)
    1

Multiplication is done with a *:

    print(3*2)
    6

Division is done with a /. Do note that the output of this is always a floating point number!

    print(6/3)
    2.0

To get the power of, use **:

    print(2**3)
    8

It's important to consider the priority of your operations as you nest mathematical operations! Do not forget BODMAS and use brackets where necessary to ensure the correct result.

You can round numbers with round(your_num, num_digits):

    print(round(8/3,2))
    2.67

We can use // to do integer division as an alternative:

    print(8//3)
    2

You can take a mathematical shortcut:

    result = result + 2

has an equivalent:

    results += 2

This can be used with the other operators as well.

The modulus function is denoted by %, giving the remainder after division.

# If else statements
The syntax is as follows:

    if condition 1 is true:
        do action 1
    elif condition 2 is true:
        do action 2
    else:
        do action 3

Note the indentation used here! The computer will test condition 1 first, and if it is false, it moves onto the next condition to test until all options are spent. We can nest multiple if/else statements within each other, being mindful of indentation.

We can use </>/<=/>= operators to compare numeric variables. We can also test for equality using == or non-equality using != within our conditions.

We can combine multiple conditions in a single statement using and, or and not:
- And requires each condition is true to be executed. 
- Or requires only a single condition to be true to be executed
- Not inverts the condition


