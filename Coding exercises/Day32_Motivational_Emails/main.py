# Import needed modules
import datetime as dt
import random
import smtplib

# Define email and password - hidden here as being uploaded to Github
dummy_email = "dummy@gmail.com"
dummy_password = "password"

# Get current day of the week
today = dt.datetime.now()
day_today = today.weekday()

# If Sunday, get a random quote and email out
if day_today == 6:
    with (open('quotes.txt') as my_file):
        contents = my_file.read().split('\n')
    selected_quote = random.choice(contents)

    # Email out
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(dummy_email, dummy_password)
        connection.sendmail(from_addr=dummy_email, to_addrs=dummy_email,
                            msg=f"Subject:Sunday Motivational Quote\n\n{selected_quote}")
