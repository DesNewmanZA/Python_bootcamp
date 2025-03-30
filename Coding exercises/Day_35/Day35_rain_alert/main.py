# Import needed modules
import requests
from twilio.rest import Client

# Define constants
API_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_key = key
weather_parameters = {
    "lat": -33.963,
    "lon": 22.461,
    "appid": API_key,
    "cnt": 4,
    "units": 'metric'
}
account_sid = sid
auth_token = token
client = Client(account_sid, auth_token)
my_number = 'masked'

# Make API call
response = requests.get(API_endpoint, params=weather_parameters)
response.raise_for_status()
data = response.json()['list']

# Loop through conditions in the next 12 hours
for period in data:
    curr_weather = period['weather'][0]
    # Classify conditions
    if curr_weather['id'] < 700:
        message = client.messages.create(
            body="Bring an umbrella! - From Des' Python project",
            from_="+18545045401",
            to=my_number,
        )
    else:
        message = client.messages.create(
            body="No rain predicted - From Des' Python project",
            from_="+18545045401",
            to=my_number,
        )
