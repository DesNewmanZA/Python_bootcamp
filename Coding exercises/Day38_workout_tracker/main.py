# Import needed packages
import requests
from datetime import datetime

# Define constants
NUTRI_APP_ID = "NutriID"
NUTRI_API_KEY = "NutriAPIkey"
NUTRI_API_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_URL = "https://api.sheety.co/mylink/workoutTracking/workouts"

headers = {
    'x-app-id': NUTRI_APP_ID,
    'x-app-key': NUTRI_API_KEY
}

# Generate new data in sheets
text = input("Tell me which exercise you did: ")

parameters = {
    "query": text
}

# Make the request for exercise
response = requests.post(url=NUTRI_API_URL, json=parameters, headers=headers)
response.raise_for_status()
data = response.json()['exercises']

# Add logged item into sheets
for item in data:
    entry_dt = datetime.now().date().strftime("%d/%m/%Y")
    entry_time = datetime.now().time().strftime("%H:%M:%S")

    new_entry = {
        "workout": {
            "Date": entry_dt,
            "Time": entry_time,
            "Exercise": item['user_input'],
            "Duration": item['duration_min'],
            "Calories": item['nf_calories']
        }
    }

    response = requests.post(SHEETY_URL, json=new_entry)