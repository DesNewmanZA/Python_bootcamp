# Import needed modules
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Define secret keys
client_ID = 'AddHere'
client_pass = "AddHere"

# Pull info from the Billboard website
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
date_string = input("Which date would you like to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date_string}", headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
songs = soup.select('li ul li h3')

# Create a list of top 100 songs
song_list = []
for song in songs:
    song_list.append(song.getText().strip())

# Log into Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_ID,
                                               client_secret=client_pass,
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private"))

user_id = sp.current_user()["id"]

# Search each song and add to a playlist
song_call = []
year = date_string.split('-')[0]
new_playlist = sp.user_playlist_create(user=user_id,
                                       name=f"{date_string} Billboard 100",
                                       public=False,
                                       collaborative=False,
                                       description='Custom playlist')

for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        sp.playlist_add_items(playlist_id=new_playlist["id"], items=[uri])
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
