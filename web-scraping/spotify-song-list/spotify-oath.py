import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests

# Spotify Authorization
SPOTIPY_CLIENT_ID='PASTE_CLIENT_ID'
SPOTIPY_CLIENT_SECRET='PASTE_CLIENT_SECRET'
SPOTIPY_REDIRECT_URI='http://example.com'


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    ) )

user_id = sp.current_user()["id"]

# Song playlist from Billboard
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url)
song = response.text
soup = BeautifulSoup(song, 'html.parser')

# save file for future
with open("billboard.html", 'w') as file:
  file.write(str(soup))

songs_name = soup.select("li ul li h3")

song_names = []

# save song list as txt
for i in songs_name:
  song_names.append(i.text.strip())
  with open(f"{date}_songs_play_list.txt", "a") as file:
    file.write("\n"+i.text.strip() + ",")

print("song list is ready")

song_uris = []
year = date.split("-")[0]

# Find uri for each song name
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# create playlist on spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
