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

# Selenium webdriver - advanced web scraping
This package can scroll, click and everything else that a human can do, making it much more powerful than Beautiful Soup.

    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("url")

    driver.close()/quit()

Close closes a single tab; quit closes the whole browser.

To search for things (using class as an example):

    from selenium.webdriver.common.by import By
    pricevar_whole = driver.find_element(By.CLASS_NAME, "class text").text

Searches are very powerful with this package - you can also search by xpath if traditional methods don't work.

You can also use find_elements to find all instances matching a search criteria.

Selenium can also be used to perform actions on a browser. Once a desired element is found, you can click it as follows:

    element.click()

There is a build-in method to locate anchor elements with a given link text to make this easier:

    my_link = driver.find_element(By.LINK_TEXT, "link text")

Combining this with the click() action can make navigating easy.

We can also find a given input box and then input text as follows:

    from selenium.webdriver.common.keys import Keys
    element.send_keys("My text", Keys.ENTER)

# Web development - backend
The frontend of a website is just what displays to the user, but to have good functionality, we need backend. The three key components to the backend are the client, the server and the database. 


## Flask
Flask is a common framework for web development in Python and provides a standardised way to deploy web apps. A framework is code that dictates the architecture of the project at hand - it is not like a library where we pick and choose when to call it. Rather, the framework calls your code so you have to cater for all possible cases. It has to be used from the start of a project. 

The environment needs to first be set up via the terminal:

    .venv\Scripts\activate
    pip install Flask

    from flask import Flask

And a basic starting app:

    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

The app variable assignment makes a Flask instance. The "/" references the home page. The @app is called a python decorator. Decorators give additional functionality to an existing function. These are referenced by @ and the function name after which the other functions are referenced as per normal.

To run the app, you would run the script as normal. Then, in the terminal:

    python -m flask --app script_name run

We can run this in a different way by referencing the current file being run (referenced by main):

    if __name__ == '__main__':
        app.run(debug=True/False)

Other NB terminal commands:
 - Print working directory: pwd
 - List items at current directory: ls
 - Change directory: cd new_path
 - Make new folder: mkdir new_folder_name
 - Make new file: touch new_file_name.ext
 - Delete file (remove): rm file_to_delete.ext
 - Go to parent folder: cd ..
 - To delete folders, go one level up: rm -rf folder_name 

We can use variable names in the url paths for the route function as so:

    <variable>

or

    <convertor: variable>

where convertor can be string, int, float, path (string but with slashes).

To create HTML, you can add it directly into the functions:

    def greet():
        return "<h1 style='text-align: center'> Hello world </h1>"

We can adjust wrappers to reference arguments using args and kwargs. For example, if we take the first defined argument:

    def decorator(function):
        def wrapper(*args, **kwargs):
            if args[0].method == True:
                function(args[0])
        return wrapper

To render HTML templates, we can use the render_template() method.

    from flask import render_template

    @app.route('/hello')
    def hello(name):
        return render_template('template.html, name=name)

The template must live inside the templates folder. Any static images/files/CSS must live inside a static folder. Static files are cached by Google Chrome so you have to press shift + refresh in order to do a hard reload if any of those change. 

To use CSS within an HTML file, add the following in the head statement:

    <link rel="stylesheet" href="static/styles.css">

Templates for websites can speed up making beautiful websites. A good set:

    https://html5up.net/

We can also get information from forms in an HTML. To do this:

    from flask import Flask, render_template, request

    @app.route('/url', methods=["POST"]):
    def method():
        if request.method == "POST":
            var = request.form['var_name']
        return render_template('index.html')

On the HTML side, the form has to look something like this:

    <form action="the_method" method="POST">
        <label for="var">Text:</label> <input type="text" id="var" name="var" placeholder="Text" value={{request.form.var}}>
        <input type="submit" value="Ok">
    </form>


## Jinja 
This allows us to use templating for when we want to create multiple pages but without necessarily redoing all the HTML etc. A good example is a blog where each post has its own page but all blog posts look the same, the only difference is the content.

If we add two {{}} around anything within our HTML, this will then be evaluated as a python expression. This is part of Jinja markup. More complex code would live in the python script and sent to the HTML. We can do this with render_template:

    render_template("index.html", num=random_number)

and this can be referenced by {{num}} in the HTML.

We can run a loop as is done with conventional python as follows:

    {% for item in list: %}

We would reference variables with {{ var_name }} and end the loop with {% endfor %}. 

We can do similar adjustments for if statements, and end with an {{% endif %}}.

If we want to create links dynamically, we can use {{url_for('function_name')}} to get it to link.

We can also include other HTML files:

    {% include "sample.html" %}

# Web development - front-end

## Bootstrap framework
This is a CSS framework. It contains pre-made CSS files that can be included into projects. It has a 12 column layout system, and gives great looking responsive websites by just adding a few classes, with good compatability.

We can use the link tag in the HTML head section to use it via the Content Delivery Network (CDN) urls:

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

We can then reference the classes (eg. btn btn-primary) when defining tags to make use of the styling. 

The bootstrap system works with an outer container (first set of div), the rows (second set of div) and the columns (third set of div). This looks like:

    <div class="container">
        <div class="row">
            <div class="col"> Hello </div>
        </div>
    </div>

Bootstrap tries to give every column equal spacing within the container. If we want to predefine how many of the 12 columns are used, we can use col-number. Eg. col-6 is 50% of the columns. 

A useful guide to the components:

    https://getbootstrap.com/docs/5.3/components/

You can also include Bootstrap directly using the bootstrap-flask package.

## Data storage using SQL
Data can be stored for website continuity. This can be done as follows:

    import sqlite3
    db = sqlite3.connect("filename.db")

If the database doesn't exist, it will be made. To insert data, we need to create a cursor to control the database. Databases can have multiple tables within them.

A table can be made as follows (as an example):

    cursor.execute("CREATE TABLE table_name (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

The primary key uniquely identifies a record. The 'not null' piec ensures that the field can't be empty. 'Unique' means no new records can have the same value. 

Data can be added in as follows:

    cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
    db.commit()

The above is using SQL more directly; however, SQLAlchemy can be used to script things a bit easier. It maps relationships in a database into objects. Each table is a separate class and each row of data is a new object. To use this, something like the below can be used:

    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
    from sqlalchemy import Integer, String, Float

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_name.db'
    db = SQLAlchemy(app)

    class Row(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(250), nullable=False, unique=True)
        rating = db.Column(db.Float(), nullable=False)

    with app.app_context():
        db.create_all()
        new_row = Row(title="some title 3", rating=9)
        db.session.add(new_row)
        db.session.commit()

The main operations can be done as follows:

### Create new record:
The primary key will be auto-generated.

    with app.app_context():
        db.create_all()
        new_row = Row(title="some title 3", rating=9)
        db.session.add(new_row)
        db.session.commit()

### Read all records: 

    with app.app_context():
        result = db.session.execute(db.select(Row).order_by(Row.title))
        all_rows = result.scalars()

### Read a single record

    with app.app_context():
        book = db.session.execute(db.select(Row).where(Row.title == "condition")).scalar()

### Update a particular record by query

    with app.app_context():
        row_to_update = db.session.execute(db.select(Row).where(Row.title == "condition")).scalar()
        row_to_update.title = "New value"
        db.session.commit() 

### Update a particular record by ID

    with app.app_context():
        row_to_update = db.session.execute(db.select(Row).where(Row.id == book_id)).scalar()
        row_to_update.title = "New condition"
        db.session.commit()  

### Delete record by primary key

    with app.app_context():
        row_to_delete = db.session.execute(db.select(Row).where(Row.id == book_id)).scalar()
        db.session.delete(row_to_delete)
        db.session.commit()

## Building beautiful websites - an overview of web design

### Colour theory
The colours selected must match the mood of the site as it conveys a message. Colour schemes can be analogous (where they pick colours close together on the colour wheel) creating a harmonious look (and so is good for navigation bars etc) or complementary (colours opposite on the colour wheel) to create a pop - this is typically not a good idea for text. There is also triadic colour schemes, that make a triangle on the colour wheel or squares. A good website to use to view these is the following:

    https://color.adobe.com/create/color-wheel

Curated colour palettes:

    https://colorhunt.co/

### Typography
Fonts also convey a message. There are serif fonts (with tails at the end of the lettering) and san serif fonts (without these tails). Serif fonts look more serious, authoratative, older; san serif fonts look more approachable, novel and contemporary. Typically, it is a good idea to stick to two fonts or so to keep a design looking clean. 

### User interface
Our eyes are naturally drawn to things in a certain order. We can exploit the hierarchy of how we view things to make things clearer and better designed - this can be done with colour by constrasting, size to pull attention, and layout. You can create more interest with layout by adding blocks of text that are just the right size - blocks that are too long feel too tedious to read but short ones can feel choppy and awkward. Alignment is also an important part to make things feel coherent and designed. Minimizing alignment points looks a lot more professional. White space is also key to highlight things. It is important to design with your audience in mind - be sure to select design elements that will be consistent with the audience you are designing for.

### User experience (UX)
We may design things but people won't necessarily interact with them the way that was intended. Making things more natural to how people interact and experience things adds for a better design. Good UX makes everything feel easy and effortless. The principles for a good UX are simplicity, consistency, reading patterns (people often look at an F or Z pattern in text), all platform design, honest design (not tricking the user into an action that is not beneficial for them).

Some designs that can provide inspiration or provoke thought:

    https://collectui.com/

# Building a REST API
REST = representational state transfer. It is an architectural style for APIs, considered the gold standard for web APIs.

We need to use HTTP request verbs (GET/POST/PUT/PATCH/DELETE) and use a specific pattern of routes/endpoint URLs. GET and DELETE can be used on all items or a specific item. POST is used to create one new item. PUT and PATCH are used for modifying a specific item. It is good practice to also return HTTP codes (see https://www.webfx.com/web-development/glossary/http-status-codes/).

An example of GET:

    @app.route("/random", methods=["GET"])
    def get_random_cafe():
        cafes = db.session.execute(db.select(Cafe)).scalars().all()
        random_cafe = random.choice(cafes)

        return jsonify(cafe = {
                        'id': random_cafe.id,
                        'name': random_cafe.name,
                        'location': random_cafe.location
                    })

This can get tedious however if dealing with larger tables. Another way of approaching this is turning the data into a dictionary and then casting to JSON. Under the table class definition, a 'to dictionary' function can be added as follows:

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

And the code can be adjusted as follows:

    @app.route("/random", methods=["GET"])
    def get_random_cafe():
        cafes = db.session.execute(db.select(Cafe)).scalars().all()
        random_cafe = random.choice(cafes)
        return jsonify(cafe=random_cafe.to_dict())

An example of POST:

    @app.route("/add", methods=["POST"])
    def add_cafe():
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            location=request.form.get("location")
        )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

PUT replaces an entire entry. PATCH updates only the needed portions. An example of PATCH:

    @app.route("/update-price/<cafe_id>", methods=["GET", "PATCH"])
    def update_price(cafe_id):
        new_price = request.args.get("new_price")
        selected_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        if selected_cafe:
            selected_cafe.coffee_price = new_price
            db.session.commit()
            return jsonify(response={"success": "Successfully updated the price."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

An example of DELETE:

    @app.route("/report-closed/<cafe_id>", methods=["DELETE"])
    def report_closed(cafe_id):
        api_key = request.args.get("api-key")
        if api_key == "TopSecretAPIKey":
            selected_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
            if selected_cafe:
                db.session.delete(selected_cafe)
                db.session.commit()
                return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
            else:
                return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        else:
            return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

Note that the postman app can be used for API testing and documentation.

# Authentication
We can make a form to get user details and store that in a database but that is not very secure. We can increase this authentication security by adding encryption with a hash function. Passwords must never be passed in plain text. Additional security can be added with password salting. This is where random characters are also added alongside prior to hashing and combined with the password to combat how people tend to make weak passwords. 