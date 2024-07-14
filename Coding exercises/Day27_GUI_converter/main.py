# Import needed modules
from widgets import *

# Define function upon button click
def button_clicked():
    meter_input = float(meters.get())
    kilometers = float(meters.get()) / 1000
    miles = kilometers * 0.621371
    km_result_label['text'] = str(round(kilometers,4))
    miles_result_label['text'] = str(round(miles,4))

# Ask for user input
button.config(command=button_clicked)

# Keep window open
window.mainloop()