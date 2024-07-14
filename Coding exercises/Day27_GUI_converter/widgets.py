# Import needed modules
from tkinter import *

# Initialize the program window
window = Tk()
window.title("Distance converter")
window.minsize(width=300, height=100)
window.config(padx= 30, pady = 30)

# Initialize all widgets on screen
meters = Entry(width=7, justify='right')
meters.grid(column=1, row=0)

meter_label = Label(text="meters", font=('Arial', 8))
meter_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", font=('Arial', 8))
is_equal_to_label.grid(column=0, row=1)

km_result_label = Label(text='', font=('Arial', 8))
km_result_label.grid(column=1, row=1)

km_label = Label(text='kilometers', font=('Arial', 8))
km_label.grid(column=2, row=1)

or_label = Label(text="or", font=('Arial', 8))
or_label.grid(column=0, row=2)

miles_result_label = Label(text='', font=('Arial', 8))
miles_result_label.grid(column=1, row=2)

miles_label = Label(text='miles', font=('Arial', 8))
miles_label.grid(column=2, row=2)

button = Button(text='Calculate')
button.grid(column=1, row=3)