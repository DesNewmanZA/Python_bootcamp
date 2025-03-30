# Import needed modules
from tkinter import *
import pandas as pd
import random
from tkinter import messagebox
import os

# Define constants
BACKGROUND_COLOR = "#B1DDC6"


# Define function to randomly select from dictionary
def new_card():
    global timer, new_word
    if len(contents) > 0:
        window.after_cancel(timer)
        canvas.itemconfig(card_img, image=card_front_img)
        canvas.itemconfig(card_title, text="French", fill='black')
        new_word = random.choice(contents)
        canvas.itemconfig(card_word, text=new_word["French"], fill="black")
        timer = window.after(3000, func=flip_card)
    else:
        messagebox.showinfo(title='Word list completed', message='You have no unlearnt words')


def flip_card():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=new_word["English"], fill='white')


def known_card():
    if len(contents) > 0:
        contents.remove(new_word)
        temp_data = pd.DataFrame(contents)
        temp_data.to_csv("data/words_to_learn.csv", index=False)
        if len(temp_data) > 0:
            new_card()
    else:
        messagebox.showinfo(title='Word list completed', message='You have no unlearnt words')


def reset_list():
    global contents
    original_data = pd.read_csv("data/french_words.csv")
    contents = original_data.to_dict(orient="records")
    os.remove("data/words_to_learn.csv")
    new_card()

# Open data needed
try:
    data = pd.read_csv("data/words_to_learn.csv")
except pd.errors.EmptyDataError:
    original_data = pd.read_csv("data/french_words.csv")
    contents = original_data.to_dict(orient="records")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    contents = original_data.to_dict(orient="records")
else:
    contents = data.to_dict(orient="records")

# Create GUI
window = Tk()
window.title("French flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create flash card using canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
card_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="French", font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, text="", font=('Arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

# Create the two buttons denoting known and unknown
right_img = PhotoImage(file='images/right.png')
wrong_img = PhotoImage(file='images/wrong.png')
right_button = Button(image=right_img, highlightthickness=0, command=known_card)
right_button.grid(column=0, row=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_button.grid(column=1, row=1)

# Create a reset button
reset_button = Button(text="Reset", highlightthickness=0, font=('Arial', 30), command=reset_list)
reset_button.grid(column=0, row=2, columnspan=2)

# Initialize cards
timer = window.after(3000, func=flip_card)
new_card()

# Keep GUI running
window.mainloop()
