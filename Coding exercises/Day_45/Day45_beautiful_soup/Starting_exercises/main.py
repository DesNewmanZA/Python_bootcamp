# Import needed modules
from bs4 import BeautifulSoup
import requests

# Pull the live website and parse it
response = requests.get("https://news.ycombinator.com/news").text
soup = BeautifulSoup(response, 'html.parser')

# Get all titles and put into a list
all_titles = soup.find_all(class_="titleline")
title_list = []
for title in all_titles:
    title_list.append(title.text)
print(title_list)

# Get all scores and put into a list
all_scores = soup.find_all(class_="score")
score_list = []
for score in all_scores:
    score_list.append(int(score.text.replace(" points", "").replace(" point", "")))
print(score_list)

# Find maximum score and associated title
max_score_pos = score_list.index((max(score_list)))
max_title = title_list[max_score_pos]
print(max_title)

