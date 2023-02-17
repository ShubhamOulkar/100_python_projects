# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
#
# with open("2023-01-01_songs_play_list.txt",'r') as file:
#     song_names = file.read()
#
# song_names = song_names.split("\n")[1:]
#
# song_uris = []
# year = date.split("-")[0]
#
# for song in range(len(song_names)):
#     if song <= 8:
#         song = song_names[song].replace(". ","")[1:]
#     elif song >= 9 and song <= 98:
#         song = song_names[song].replace(". ", "")[2:]
#     elif song >= 99:
#         song = song_names[song].replace(". ", "")[3:]
#
#     result = sp.search(q=f"track:{song} year:{year}", type="track")
#     print(result)
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")
#


# Song playlist from Billboard

from bs4 import BeautifulSoup
import requests

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

for i in songs_name:
  song_names.append(i.text.strip())
  with open(f"{date}_songs_play_list.txt","a") as file:
    file.write("\n"+i.text.strip() + ",")

print("song list is ready")

