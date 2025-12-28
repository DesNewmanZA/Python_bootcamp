# Include needed modules
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define global variables
URL = "https://en.wikipedia.org/wiki/List_of_birds_of_South_Africa"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; Python scraping for learning purposes)"
}

# Get the information loaded at the URL
url_response = requests.get(URL, headers=HEADERS)
url_response.raise_for_status()

# Use Beautiful Soup to scrape - the tables contain the bird names
soup = BeautifulSoup(url_response.text, 'html.parser')
bird_tables = soup.find_all("table", class_="wikitable")

# Extract all bird names and if they are a vagrant or not
bird_names = []
for table in bird_tables:
    rows = table.find_all("tr")[1:]
    for row in rows:
        cells = row.find_all("td")
        if len(cells) < 3:
            continue

        bird_name = cells[0].get_text(strip=True)
        bird_status = cells[2].get_text(strip=True).upper()

        # Only keep status if it is a vagrant
        if "VAGRANT" in bird_status:
            bird_names.append([bird_name, "Vagrant"])
        else:
            bird_names.append([bird_name, ""])

# Make a pandas dataframe
df = pd.DataFrame(bird_names, columns=['Bird name', 'Status'])
print(df)
