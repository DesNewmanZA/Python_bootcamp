# Import needed modules
import requests

# Define parameters
parameters = {
    'amount': 10,
    'type': 'boolean'
}

# Make API call to get questions
response = requests.get(url='https://opentdb.com/api.php', params=parameters)
response.raise_for_status()
question_data = response.json()['results']