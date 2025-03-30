# Import needed modules
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from string import ascii_lowercase, ascii_uppercase
import pyperclip

# Define reference list of letters, numbers and symbols
letters = list(ascii_lowercase + ascii_uppercase)
numbers = [str(i) for i in range(0, 10)]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']  # Kept hardcoded as not all symbols are useful in a password


######################
# PASSWORD GENERATOR #
######################
def generate_password():
    # Generate and append random symbols, numbers and letters
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]
    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    pwd_list = symbol_list+number_list+letter_list

    # Shuffle the selected characters
    shuffle(pwd_list)
    generated_pwd = ''.join(pwd_list)
    pass_text.insert(0, generated_pwd)
    pyperclip.copy(generated_pwd)

#################################
# SAVING PASSWORD FUNCTIONALITY #
#################################
def save():
    if len(web_text.get()) > 0 and len(email_text.get()) > 0 and len(pass_text.get()) > 0:
        # Pop up a message box to confirm what's happening
        is_fine = messagebox.askokcancel(title=web_text.get(), message=f"Details entered:\nEmail: {email_text.get()}, \
                                            \nPassword: {pass_text.get()}\nAre these details correct?")

        # Append onto file
        if is_fine:
            with open('password_list.txt', mode='a') as my_file:
                my_file.write(f"{web_text.get()} | {email_text.get()} | {pass_text.get()}\n")

            # Clear existing info
            pass_text.delete(0, END)
            web_text.delete(0, END)
    else:
        messagebox.showinfo(title="Error! Missing fields", message="Please do not leave any fields blank.")


#############
# GUI SETUP #
#############
# Initialize window with title and some padding
window = Tk()
window.title('Password manager')
window.config(padx=50, pady=50)

# Make a canvas with the logo as the main feature
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Make the entry boxes needed
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
web_text = Entry(width=35)
web_text.grid(column=1, row=1, columnspan=2)
web_text.focus()

email_label = Label(text="Email/username:")
email_label.grid(column=0, row=2)
email_text = Entry(width=35)
email_text.grid(column=1, row=2, columnspan=2)
email_text.insert(0, 'despinanewman@gmail.com')

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)
pass_text = Entry(width=16)
pass_text.grid(column=1, row=3, columnspan=1)

generate_button = Button(text='Generate password', width=15, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=20, command=save)
add_button.grid(column=1, row=4, columnspan=2)

# Keep the window running
window.mainloop()
