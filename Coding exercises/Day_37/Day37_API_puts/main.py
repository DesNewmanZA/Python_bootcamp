# Import needed modules
import requests
from datetime import datetime

# Create constants
USERNAME = "desnewman"
TOKEN = "asdfghjkl"
MY_GRAPH = "graph1"

# Create a new user
pixela_endpoint = "https://pixe.la/v1/users"
create_user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': "yes",
    'notMinor': "yes"
}
# response = requests.post(url=pixela_endpoint, json=create_user_params)
# print(response.text)

# Make new graph
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# print(graph_endpoint)
# graph_params = {
#     'id': 'graph1',
#     'name': 'My coding commits',
#     'unit': 'commit',
#     'type': "int",
#     'color': "shibafu"
# }
# headers = {
#     'X-USER-TOKEN': TOKEN
# }
#
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

# Add a new pixel
mygraph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{MY_GRAPH}"
headers = {
    'X-USER-TOKEN': TOKEN
}

# today = datetime.now()
today = datetime(year=2024, month=6, day=1)
str_today = today.strftime("%Y%m%d")

mygraph_params = {
    'date': str_today,
    'quantity': '2'
}

response = requests.post(url=mygraph_endpoint, json=mygraph_params, headers=headers)
print(response.text)