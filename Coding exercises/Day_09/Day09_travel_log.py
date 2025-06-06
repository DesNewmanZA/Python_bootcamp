# Take in inputs - assume correct form
country = input() 
visits = int(input()) 
list_of_cities = eval(input()) 

# Assume a starting point in the travel log
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

# Function that adds new countries to the travel log
def add_new_country(country, visits, list_of_cities):
  new_dict = {
              "country": country,
              "visits": visits,
              "cities": list_of_cities
  }
  travel_log.append(new_dict)

# Output travel log after adding latest city
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")