# Import needed modules
from bs4 import BeautifulSoup
import requests

# Pull the live website and parse it
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                        "-movies-2/").text
soup = BeautifulSoup(response, 'html.parser')

# Extract all movie titles - extract article title description first and then select the titles
all_titles = soup.find_all(name="h3", class_='title')
title_list = []
for title in all_titles:
    title_list.append(title.text)

# Sort the movies and convert into a text file
title_list.reverse()
with open('movies.txt', 'w', encoding="utf-8") as f:
    for title in title_list:
        f.write(f"{title}\n")

