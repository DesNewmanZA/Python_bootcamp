# Import needed modules
import datetime as dt
import random
import smtplib
import pandas as pd
import os

# Define email and password - hidden here as being uploaded to Github
dummy_email = "dummy@gmail.com"
dummy_password = "password"

# Get current date
today = dt.datetime.now().date()

# Get list of all birthdays
birthdays = pd.read_csv('birthdays.csv')
birthdays['birthday'] = pd.to_datetime(dict(year=birthdays.year, month=birthdays.month, day=birthdays.day))

# Search and see if today matches anyone's birthday
people_to_wish = (birthdays[(birthdays.month == today.month) & (birthdays.day == today.day)][['name', 'email']])
people_to_wish = dict(people_to_wish.values)

# If there are people to wish, select random letter for each and replace their names in the text
if len(people_to_wish) > 0:
    for key, value in people_to_wish.items():
        selected_letter = random.choice(os.listdir('letter_templates'))
        with open(f'letter_templates/{selected_letter}') as my_file:
            contents = my_file.read().replace("[NAME]", key)

        # Send emails out
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(dummy_email, dummy_password)
            connection.sendmail(from_addr=dummy_email, to_addrs=value,
                                msg=f"Subject:Happy birthday!\n\n{contents}")