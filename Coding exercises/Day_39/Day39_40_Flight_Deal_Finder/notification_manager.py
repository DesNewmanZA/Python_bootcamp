# Import needed modules
from twilio.rest import Client
import smtplib

# Define constants
account_sid = sid
auth_token = token
my_number = 'masked'
my_email = 'masked'
my_email_pwd = 'masked'
my_smtp = 'masked'

# Class to manage notifications if flights are cheaper than the lowest price stored
class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)
        self.smtp_address = my_smtp
        self.email = my_email
        self.email_password = my_email_pwd
        self.connection = smtplib.SMTP(my_email)


    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_="+18545045401",
            body=message_body,
            to=my_number
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_email(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New lowest price flight!\n\n{email_body}".encode('utf-8')
                )