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

You can give a module an alias to refer to it quicker:

    import module as md

This will allow us to access things from the module as follows:

    md.method_name()

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

We can index items in a list (called list slicing using a colon). Note that the last element is not inclusive if it is specified. These indeces can be negative eg. -1 gets the last element of the list. You can add a 2nd colon to add the jump size.

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

If we want, we can define input and output types:

    def my_function(var1: int) -> bool

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

# Classes and objects
Objects can be thought of in terms of what they have (attributes - the variables attached to it) and what they do (their methods they perform). Classes hold a template of what objects have and do, and instances of them are called objects. Classes usually have each word's first letter capitalised.

When an object is defined, we can call the object's attributes as follows:

    my_object.my_attribute

To use an object's methods:

    my_object.my_method(vars)

To make a class with nothing in it to start off:

    class ClassName:
        pass

We can add attributes to the class as so:

    my_object = ClassName()
    my_object.my_var = value

But this is a bit prone to error so rather we can specify the starting attributes of an object. We can do this with the init constructor to define the starting values:

    class ClassName:
        def __init__(self, value):
            self.field = value
            self.field2 = default_value 

    my_object = ClassName(value)

We can add functions inside the class as per normal; the only difference is the first parameter is always self.

Classes have inheritance of both attributes and methods from other classes. An example is shown below.

    def SubClass(MainClass):
        def __init__(self):
            super().__init__()

        def my_method(self):
            super().my_method()
            # Add extra functionality for the subclass 

# Installing packages
You can install other packages by going to the python command prompt and typing:

    pip install package_name

A list of available packages can be found here:

    https://pypi.org/

# Tuples
These are denoted as follows:

    my_tuple = (val1, val2, ..., valn)

These are immutable. That is, they can't be changed. These are important for storing data you are sure must not be changed.

# Event listeners
An event listener is a function or method that detects and responds to events within a program or application. When attached to an object or element, the listener waits for a specific event to occur, such as a button click, mouse movement, or keyboard input.

# Higher order functions
These are functions that work with other functions. Note that if a function is passed to a higher order function as an argument, it doesn't require the brackets passed too.

# Working with files
We can open a file using Python - we first need to open the file and then read in the contents, and then close it when we are done with it. The default way to open a file is read-only (mode = 'r').

    my_file = open('my_file.txt')
    contents = my_file.read()
    my_file.close()

Another way to do this without having to explictly close the file is as follows:

    with open('my_file.txt') as my_file:
        contents = my_file.read()

If we want to write to a file, we can accordingly do this:

    with open('my_file.txt', mode='w') as my_file:
        my_file.write("Additional text")

This will replace all contents of the file from scratch as it is essentially recreating the file anew. If this file doesn't exist and mode of write has been selected, the file will be made automatically.

If we want to just add lines of code, we can make the mode = 'a' for appending. 

When we are specifying paths for locating files, we can give the absolute file path (the full path that would be used in a file explorer), or we can deal with relative paths which start from where the code is saved and navigate from there.

To go into folders further nested within, we start with a '.' and specify the next folders. If we want to go a folder back, we use a '..'.

    ./Next_folder/my_file.txt
    ../Higher_folder/other_file.txt

If you want to go up multiple folders, we repeat the ../ as many times as needed.

# Working with data
Python has a library for dealing with csv files, with an associated reader. This stores each row in the data as a list.

    import csv

    with open('weather_data.csv') as my_file:
        contents = csv.reader(my_file)

This can be quite cumbersome, so the pandas library is often used instead to deal with data more simply. The above can be replaced as so:

    import pandas as pd
    my_df = pd.read_csv('weather_data.csv')

This will automatically assign heading names to the data (if no instruction to the contrary is given) and the columns can be referenced by their names (case-sensitive):

    my_col = my_df['var_name']
or

    my_col = my_df.var_name

The format of the full data is a data frame; a single column is a series.

If we want to get hold of rows, we define the column we want to search to search through and add a condition in the square brackets:

    my_rows = my_df[my_df['var_name]==condition]

If you want to make a data frame from scratch, this can be done using a dictionary of data:

    my_df = pd.DataFrame(data_dict)

We can output data frames as a csv:

    my_df.to_csv('csv_name.csv')

# List and dictionary comprehension
This can be used to create new lists without a for loop. An example of this is:

    my_list = [new_item_rule for item in list if condition]

This can be used with any iterable data type.

    my_dict = {new_key:new_item for item in list if test}

or 

    my_dict = {new_key:new_item for (key,item) in dict.items() if test}

You can also loop through a data frame in a similar way to dictionaries. But you can also iterate over the rows:

    for (index, row) in my_df.iterrows:
        conditions

# GUIs and Tkinter
Tkinter allows us to make GUIs. It's a module you need to import - to make a window, we would initialize it and keep 'listening' for user input until a certain condition is met (done via mainloop).

    import tkinter
    window = tkinter.Tk()
    window.title("Header title of window")
    window.minsize(width=x, height=y)
    
    # Components must be initialized and their placement specified to appear
    label = tkinter.Label(text="Label text", font=('Arial', 20, 'bold'))
    label.pack()

    def button_clicked():
        print("I got clicked!")

    button = tkinter.Button(text='Click me!', command = button_clicked)
    button.pack()

    input = tkinter.Entry()
    input.insert(END, string="Some text to begin with.")
    input.pack()
    user_input = input.get()

    text = tkinter.Text()
    text.focus() # Puts cursor here

    def spinbox_used():
        print(spinbox.get())
    
    spinbox = tkinter.Spinbox(from_=0, to=10, command=spinbox_used)
    spinbox.pack()

    def scale_used(value):
        print(value)

    scale = tkinter.Scale(from_=0, to=100, command=scale_used)
    scale.pack()

    def checkbutton_used():
        print(checked_state.get())
    
    checked_state = tkinter.IntVar()
    checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
    checked_state.get()
    checkbutton.pack()

    def radio_used():
        print(radio_state.get())

    radio_state = tkinter.IntVar()
    radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
    radiobutton2 =tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
    radiobutton1.pack()
    radiobutton2.pack()

    def listbox_used(event):
        print(listbox.get(listbox.curselection()))

    listbox = tkinter.Listbox(height=4)
    fruits = ["Apple", "Pear", "Orange", "Banana"]
    for item in fruits:
        listbox.insert(fruits.index(item), item)
    listbox.bind("<<ListboxSelect>>", listbox_used)
    listbox.pack()

    # Must be the last thing in the code
    window.mainloop()

We can treat the label like a dictionary and update it later on:

    label['text'] = 'my new text'

Pack will automatically put widgets from top to bottom. The side parameter can be used to define exactly where to stack them. If you want a precise position, pack won't do the job.

Place is used for precise positioning. The coordinates (0, 0) is the top left corner.

    label.place(x=coord, y=coord)

There is also grid that splits the window into a grid.

    label.grid(column=num, row=num)

This one is relative to other widgets. It's easiest to start in order from top left onwards. You can only use one of pack/grid/place. We can use columnspan to make things go over multiple columns.

We can also change padding around the window:

    window.config(padx=num, pady=num)

We can use the canvas widget to layer things. 

    canvas = tkinter.Canvas()

We can also make pop-up message boxes:

    from tkinter import messagebox
    messagebox.showinfo(title='title', message='message')
    messagebox.askokcancel(title='title', message='message')

# Advanced python arguments
We can initialise functions with default values. That way, if these are not explictly defined/passed on a function call, the default values will be used:

    def my_funct(a=1, b=3, c=6):
        code

We can also create functions that can take an unlimited number of arguments (*args). For example, if we want to write a simple program that sums up an unlimited amount of inputted numbers. This can be done via *args as it takes the inputs in and converts them into a tuple:

    def add(*args):
        sum = 0
        for n in args:
            sum += int(n)
        return sum

We can also deal with an unlimited amount of keyword arguments (**kwargs).  These become a dictionary. 

    def calculate(**kwargs):
        kwargs[key] = value
        code

The problem with the above is it will throw an error if the key doesn't exist. And so, it is better to use the get function instead.

# Exception handling
Key errors are when we look for something in a dictionary that doesn't exist. Index errors are when we look at an index that doesn't exist. A type error is when we try do an operation on something that can't be done on the data type. We can try plan for and handle these cases.

    try:
        Will try this but may give errors
    except:
        If the try fails, do this
    else:
        Do if there were no exceptions
    finally:
        Do this no matter what happens

Our exceptions should usually be clarified for the exception type. We can use a qualifying type:

    try:
        Code to try
    except FileNotFoundError:
        Do this
    except KeyError:
        Do this

You can grab the error message as well:

    try:
        Code to try
    except KeyError as error_msg:
        Do this and can reference error_msg

We can also raise our own exceptions:

    raise TypeError("Your error message here")

This can be useful for validating inputs eg. ValueError

# JSON files
This stands for JavaScript Object Notation and is a standardised way of transmitting text data. It can look a bit like a dictionary:

    {
    "employees":[
        {"firstName":"John", "lastName":"Doe"},
        {"firstName":"Anna", "lastName":"Smith"},
        {"firstName":"Peter", "lastName":"Jones"}
    ]
    }

To write to a JSON, we use json.dump():

    import json
    json.dump(dictionary, my_file, indent=nums)

To read data from a JSON:

    import json
    json.dump(my_file)

If we want to add to a JSON:

    import json
    json.update()

General format for taking an existing JSON and updating it:

    import json
    with open('my_file.json', mode='r') as my_file:
        my_data = json.load(my_file)
        my_data.update(new_data)
    with open('my_file.json', mode='w') as my_file:
        json.dump(my_data, my_file, indent=4)

# Emailing with Python
SMTP = Simple Mail Transfer Protocol. Used to send and receive messages. We use smtplib and start tls which allows us to secure a connection to the server.

    import smtplib
    connection = smtplib.SMTP(smtpserver)
    connection.starttls()
    connection.login(user='emailaddress', password='password')
    connection.sendemail(from_add='email', to_addrs='email', msg='Subject:text\n\nContents of email.')
    connection.close()

This requires an app password in Gmail.

# Working with dates and time
You can use datetime to get current dates as well as deal with dates. To get the current date and time:

    import datetime as dt
    dt.datetime.now()

You may want to break this apart eg. get the year.

    dt.datetime.now().year()

To make a new date, the following can be done:

    dt.datetime(year=, month=, day=, optional time inputs)

# Cloud hosting
If we want an application to be continuously running and checking,we can host it in the cloud and get it to execute periodically. A good option for this is:

    https://www.pythonanywhere.com/

We can upload the scripts we want to execute. Then we will start a new bash session. If the script is called main.py,

    python3 main.py

This will test if it is working fine. We can then schedule it accordingly, specifying a time and giving the command that must be run.

# Application Programming Interfaces (APIs)
These define how information is communicated between two different applications. You will use the rules from an API to pull data with the appropriate structured response. 

You need to know the API endpoint (eg. location of the data). You also need to make a request over the interest to do this - it has checks and balances in place.

To do these calls:

    import requests
    response = requests.get(url='APIendpoint')

You won't see JSON data directly if you print this but rather the response code. These tell us if our request was successful or failed. The famous example is 404 (not found). You can tell what their meaning is at a high level by their first digits:

- 1xx: hold on
- 2xx: successful
- 3xx: permission denied
- 4xx: user error
- 5xx: server error

Code 200 is successful. A comprehensive list can be seen here:

https://www.webfx.com/web-development/glossary/http-status-codes/

We can raise exceptions based on the codes:

    response.raise_for_status()

To get the data, something like this will be done:

    data = response.json()

APIs also have parameters, and these allow us to give an input when making a call.

Sometimes APIs can return results with HTML entities, which make it not very readable. This can be corrected as follows:

    import html
    html.unescape('symbol')

Certain APIs need keys to authenticate you. 

A list of free APIs: https://apilist.fun/

There are other types of requests other than just getting data. The 4 main types are: get, post, put, delete. A good example of post is using the Google Sheets API to write into a sheet. Put is when you update data already existing. Delete is to get rid of existing data.

    import requests
    response = request.post(url='myurl', json='myparams')

# Environment variables
If we go into the terminal and type env, we will get a list of information about the running environment we are using. We can set variables at an environment level rather than adjusting our code which is convenient, and it's also good for security when uploading code. We can save these variables as follows in the terminal:

    export var_name=content; export var_name2=content2

If you retype env, you will see that environment saved. To use these:

    import os
    content = os.environ.get("my_var")

# Web development
Websites consist of HTML, CSS and Javascript files for the most part. Each do a different job:
- HTML gives the structure of the website/layout
- CSS files are responsible for styling the website
- Javascript allows the website to actually do useful things.

## HTML
HTML stands for Hyper Text Markup Language. It links together pieces of information and helps structure the information accordingly with tags (eg. bold, italic, headings etc). Tags define the structure and take the form:

    <tag> content </tag>

Tags can also have attributes in them giving extra customizability:

    <tag class='option'> content </tag>

These attributes have information that you don't want to actually appear, such as a reference to create links.

Some elements, such as images, are not related to formatting content and thus do not need a closing tag:

    <img src='path' />

To start HTML documents, we need to initialize it as follows (the boilerplate):

    <!doctype html>
    <html lang="en">
        <head>
            <meta charset="UTF-8"/>
            <meta name="viewport" content="width=device-width"/>
            <title> my title </title>
        <\head>
        <body>
            content here
        <\body>
    </html>

We can define the < head > element - this is a container for everything you want on the page that isn't the content in the page eg. keywords, page descriptions, CSS for formatting etc.

We can mark up headings of various sizes use tags h1 to h6 from largest to smallest.

Comments can be made using < !-- and -- > (without the spaces).

Paragraphs are denoted by < p >. 

Lists can be unordered < ul > or order < ol >, with each list item denoted by < li >.

Links can be made with a < a > and referenced as so:

    <a href="URL"> Content </ a>

A great set of references for HTML can be found here: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements

We can do a horizontal rule as follows:

    <hr/>

We can do breaks as follows:

    <br/>

# CSS
This stands for Cascading Style Sheets and is used to make websites look beautiful. It informs the HTML what styling to use. A good reference is here: https://www.w3schools.com/cssref/index.php.

There are 3 methods of inclusion:

- **Inline:** < tag style='css'/ >. This specifies the CSS into the HTML. 
Example: < html style = "background: blue" > < / html >. Useful for styling a specific element. Can make code messy so not recommended for the full document.
- **Internal:** < style > css < style / >. Example: < style > html {background: red;} < style / >. Often goes in the head but can go anywhere and be applied to whatever elements we pick. Ok for simple websites but can grow large for big websites.
- **External:** < link href="style.css" / >. Similar to internal except this is all stored in a separate file which keeps it neat. We include it into the HTML as follows: < head > < link  rel="stylesheet" href="./styles.css" / > < / head>.

CSS is structured by selectors, which define which part of the HTML we want to style. An example below selects the h1 headings and formats those:

    h1 {
        color: blue
    }

Class selectors are as follows:

    .red-heading {
        color: red
    }

This allows us to define a class eg. red-heading. These can then be added to any element:

    <h2 class="red-heading">

There are also ID selectors.

    #main {
        color: red
    }

These select all elements with a particular ID attribute. Example:

    <h2 id="main">

ID selectors should be used for single elements; class ones can be used for many elements.

There are also attribute selectors, formatting specific attributes eg. href, src, alt etc.

    p[href]{
        color: red
    }

Universal selectors apply to all elements:

    *{
        color: red
    }

Common colour properties (common color names here https://developer.mozilla.org/en-US/docs/Web/CSS/named-color):
- background-color
- color

When we assign a non-standard named colour, we can use the colour's hex code to do so. 

    h1 {
        color: #5D3891
    }

We can adjust the font we use too:

    h1 {
        font-weight: bold/bolder/lighter;
        font-size: 20px/12pt;
        font-family: Helvetica, sans-serif (specific and then backup font)
        text-align: center/left/right
    }

If we want a relative font size, we can use 2em/2rem for example to go twice the reference size for an element. 

Margins, padding and borders are also important CSS elements. We can define things such as height and width of elements:

    height: 100%/200px
    width: 100%/200px

We can add borders:

    border: 10px solid black

The border can even be specified one side at a time:

    border: 30px solid black;
    border-width: 0px 10px 20px 30px

We can add padding - this goes before the border:

    padding: 20px

We can also add margins - these go after the border:

    margin: 10px

We make boxes around our elements via content division tags. 

    < div > content < /div>

# Web scraping with beautiful soup
Web scraping allows us to take data from a website by extracting it from the HTML file. This is done with a library called Beautiful Soup (documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

An example of use:

    from bs4 import BeautifulSoup

    with open('website.html') as my_file:
    contents = my_file.read()

    soup = BeautifulSoup(contents, 'html.parser')

If the html.parser is not working, trying the lxml one may be a better way forward.

Once turned into soup, we can then pull out specific elements:

    web_title = soup.title

We can put .name to give the html tag, and we can put .string to get hold of just the contents. This will however only retrun the first instance. If we want all, we need to go:

    soup.find_all(name = tag_name)

In combination with the getText() function, this can parse all content. We can go more general and use .get("reference") to find something like all the hrefs.

We can also search by class, id etc. rather than just name.

If we take the soup and use .prettify(), this will indent the soup for easier reading.

