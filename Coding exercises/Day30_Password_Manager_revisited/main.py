# Import needed modules
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from string import ascii_lowercase, ascii_uppercase
import pyperclip
import json

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
def save_password():
    entry_dict = {
        web_text.get(): {
            'email': email_text.get(),
            'password': pass_text.get()
        }
    }

    if len(web_text.get()) > 0 and len(email_text.get()) > 0 and len(pass_text.get()) > 0:
        # Read in data with handling for if the file doesn't exist
        try:
            with open('password_list.json', 'r') as my_file:
                my_data = json.load(my_file)
        except FileNotFoundError:
            with open('password_list.json', mode='w') as my_file:
                json.dump(entry_dict, my_file, indent=4)
        # Write into the file
        else:
            # If key exists, ask user if they are willing to overwrite the existing info
            try:
                my_data[web_text.get()]
                replace = messagebox.askokcancel(title=f"Website already exists",
                                                 message="Website data exists in data. Replace?")
                if replace:
                    my_data.update(entry_dict)
                    with open('password_list.json', mode='w') as my_file:
                        json.dump(my_data, my_file, indent=4)
            # If key doesn't exist, write to data history
            except KeyError:
                my_data.update(entry_dict)
                with open('password_list.json', mode='w') as my_file:
                    json.dump(my_data, my_file, indent=4)
            pass_text.delete(0, END)
            web_text.delete(0, END)

    else:
        messagebox.showinfo(title="Error! Missing fields", message="Please do not leave any fields blank.")


###################
# PASSWORD LOOKUP #
###################
def find_password():
    # Only search if website field is populated
    if len(web_text.get()) > 0:
        # Read in data with handling for if the file doesn't exist
        try:
            with open('password_list.json', 'r') as my_file:
                my_data = json.load(my_file)
        except FileNotFoundError:
            messagebox.showinfo(title=f"No data",
                                message=f"There is no data stored in the password manager at present.")
        # Find associated entry
        else:
            try:
                entry = my_data[web_text.get()]
                pass_text.delete(0, END)
                email_text.delete(0, END)
                pass_text.insert(0, entry['password'])
                email_text.insert(0, entry['email'])
            except KeyError:
                messagebox.showinfo(title=f"Details for {web_text.get()}",
                                    message=f"This website's details are not stored in the data.")
    else:
        messagebox.showinfo(title=f"Invalid search",
                            message=f"Please input a valid website to search for.")


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
website_label.grid(column=0, row=1, padx=5, pady=5)
web_text = Entry(width=35)
web_text.grid(column=1, row=1, columnspan=2, padx=5, pady=5)
web_text.focus()

email_label = Label(text="Email/username:")
email_label.grid(column=0, row=2, padx=5, pady=5)
email_text = Entry(width=35)
email_text.grid(column=1, row=2, columnspan=2, padx=5, pady=5)
email_text.insert(0, 'despinanewman@gmail.com')

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3, padx=5, pady=5)
pass_text = Entry(width=35)
pass_text.grid(column=1, row=3, columnspan=1, padx=5, pady=5)

generate_button = Button(text='Generate password', width=15, command=generate_password)
generate_button.grid(column=3, row=3, padx=5, pady=5)

add_button = Button(text="Add", width=20, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, padx=5, pady=5)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=3, row=1, padx=5, pady=5)

# Keep the window running
window.mainloop()
