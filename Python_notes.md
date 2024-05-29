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

If we want to get a subset, we can do the following (not inclusive of end point):

    print("Hello"[1:3])
    el

    print("Hello"[0:2])
    he

If you want Python to just read text without handling for special cases (for example, reading in a file path), preface the string with r to indicate a raw string

    print(r'This doesn't need anything special!')

Strings are immutable - that is, we can't edit a string.

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

Note the indentation used here (4 spaces or one tab - spaces are preferred)! The computer will test condition 1 first, and if it is false, it moves onto the next condition to test until all options are spent. We can nest multiple if/else statements within each other, being mindful of indentation.

We can use </>/<=/>= operators to compare numeric variables. We can also test for equality using == or non-equality using != within our conditions.

We can combine multiple conditions in a single statement using and, or and not:
- And requires each condition is true to be executed. 
- Or requires only a single condition to be true to be executed
- Not inverts the condition

# Randomisation
There is a library in Python that can assist us in generating random numbers. We can bring it into our code as follows:

    import random

If we want a random integer between a certain range:

    random_int = random.randint(start, end)

If we want a random number between 0 and 1:

    random_float = random.random()

If we want a random floating number between certain ranges, we can multiply it by the end range to get a random float between 0 and end range point.

We can select an item from a list randomly as follows:

    random.choice(my_list)

We can shuffle a list randomly and in place as follows:

    random.shuffle(my_list)

# Modules
We don't always need to keep everything in the same script to be able to access it. The random library mentioned above is an example of this - this is called a module. You can import modules and access functions and variable definitions from it.

For example, if you have a script saved called my_module that stores the value of pi in a variable named pi, we can access it as follows:

    import my_module
    print(my_module.pi)

# Lists
Lists are a data structure, used to organise data in Python that is part of the same collection. They can contain any types of data together. Their syntax is as follows:

    my_list = [item 1, item 2, ..., item n]

These items do have an order and this can be useful too. You can index them as you do strings.

You can adjust items in a list:

    my_list[1] = "my adjustment"

If you want to add an item to an end of a list:

    my_list.append("New item")

You can add on another list using extend:

    my_list.extend([item1, item2])

Lists are mutable - we can change what is stored in them. Note that if we assign a list into a new variable without making a copy, any operations done on the new variable will affect the old variable too. The safest thing is to make a copy:

    new_list = my_list.copy()

You can make nested lists to link related data together. To access sub-lists, we just add more indexing brackets:

    nested_list[1][3]

# For loops
Used to repeat something a predetermined number of times. 

To use for loops with a list:

    for item in list_of_items:
        do action

To use for loops without a list, the range function is very useful to determine how many times we should run things.

    for number in range(a, b, step):
        do action

Note that the start point a is included but not the end point b.

# Functions
There are plenty of built-in functions. A good reference is here:
https://docs.python.org/3/library/functions.html

Functions always are denoted by brackets, taking in an input.

Custom functions can be written as follows:

    def my_function_name(input1, ..., inputm):
        actions

The function is the called as follows:

    my_function_name(input1, ..., inputm)

The variables being inputted are called parameters, and the actual values of those parameters are called the arguments.

Python functions are by default positional arguments. That is, without further specification, python will assign the arguments in the order they're defined in the function. The parameters can be explicitly defined when arguments are passed to disregard the ordering - this is called keyword arguments.

    my_function(b=input1, c=input2, a=input3)

When we want to output things, we use the return function:

    def my_function(input):
        actions
        return output

If we assign this as a variable, the output will be assigned to this variable:

    output = my_function(input)

Note that when a return function is executed, the function exits and nothing further is examined.

# Style guide
It's best practice to follow the recommended style for your code. This can be found here:
https://peps.python.org/pep-0008/

# While loops
These are best used to loop when we don't have a predetermined number of times to loop for upfront, and are rather looking for a condition to be satisfied. Syntax:

    while condition is true:
        do action

# Dictionaries
Dictionaries store keys that we can use to look up things, and then an associated value with some information stored about the key. Syntax:

    dictionary = {key : value, key2 : value2}

Typical formatting is leaving the { on the line where it is defined, each entry on a new line with a tab, and the } in line with the definition.

To fetch items from a dictionary:

    my_dict[key]

If we add new items or edit an existing item:

    my_dict[key] = value

Looping through a dictionary with a for loop will only give you the key. So if you want the value, you would loop using that key. Note that values can be anything - even lists and other dictionaries.

# Docstrings
These allow us to add documentation in our functions to help explain what we are doing.

These go right after the function definition and they are defined by 3 quotation marks:

    def my_function(input):
        '''Your document strings 
                - can be multiline'''
        actions
        return output

# Scope
If we want to modify a global variable inside a function without explicitly passing it in as an input, something like the following can be done:

    my_var = 1

    def my_funct():
        global my_var
        my_var += 1

This is prone to causing errors though, so this is often not a desired way to go about modifying global variables. Instead, it's more common to return the output.

Global constants are useful for anything that shouldn't change. The convention for these variables is to use all upper case for these:

    PI = 3.14