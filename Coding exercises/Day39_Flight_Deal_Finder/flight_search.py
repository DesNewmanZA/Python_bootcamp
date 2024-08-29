# Import needed modules
import requests

# Define constants
FLIGHT_API_KEY = "TMKoIeqC9bvBhftferRVyAMeC2ysz9Pf"
FLIGHT_API_PWD = "rNi5GUGqireGkJda"
FLIGHT_API_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
CITY_SEARCH_URL = "https://test.api.amadeus.com/v1/reference-data/locations/cities"


# Class that will handle flight searching and associated tasks
class FlightSearch:
    # The flight search uses a key, a secret code and a generated token accordingly
    def __init__(self):
        self._api_key = FLIGHT_API_KEY
        self._api_secret = FLIGHT_API_PWD
        self._token = self.get_new_token()

    # This fetches the IATA codes where they are missing
    def get_destination_code(self, city_name):
        # Initialize required header
        headers = {"Authorization": f"Bearer {self._token}"}
        # Initialize search query
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        # Make API request
        response = requests.get(
            url=CITY_SEARCH_URL,
            headers=headers,
            params=query
        )

        # Error handling - populate if possible, else define outputs for index/key errors
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code

    # Generate new token for API calls
    def get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_URL, headers=header, data=body)

        return response.json()['access_token']

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct = True):
        # Define headers
        headers = {"Authorization": f"Bearer {self._token}"}
        # Define query to search for
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": "10",
        }

        # Make an API request
        response = requests.get(
            url=FLIGHT_API_URL,
            headers=headers,
            params=query,
        )

        # Error handling
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()
