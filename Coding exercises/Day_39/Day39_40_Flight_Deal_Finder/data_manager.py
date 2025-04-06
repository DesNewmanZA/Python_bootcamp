# Import needed modules
import requests

# Define constants
SHEETY_URL = "PRICES_SHEET_URL"
SHEETY_USERS_URL = "USERS_SHEET_URL"

# Data manager will take data from Google sheets and update codes for the city
class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    # Get all destination data in the Google sheet
    def get_destination_data(self):
        response = requests.get(url=SHEETY_URL)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    # Update the IATA codes
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_URL}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_URL)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
