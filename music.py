import requests
from bs4 import BeautifulSoup
# key = '416052b76afffaa1ae757c4d3c7a30f1'
# url = 'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}'
# response = requests.get(url)
# print (response)

# song name
# <div tabindex="-1" role="checkbox" dir="auto" aria-checked="false" class="songs-list-row__song-name">Alone</div>

# song artist
# <div class="songs-list__song-link-wrapper" dir="auto">
#        <a href="https://music.apple.com/us/artist/night-lovell/954917315" class="songs-list-row__link" tabindex="-1">Night Lovell</a>
# </div>


response = requests.get(
    "https://music.apple.com/us/playlist/a/pl.u-mJy81vRulNv43Z")
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)
song_titles = soup.findAll('div', attrs={"class": "songs-list-row__song-name"})
song_artist = soup.findAll(
    'div', attrs={"class": "songs-list__col--artist"})

artist = []
for i in song_artist:
    for x in i.findAll('div', attrs={"class": "songs-list__song-link-wrapper"}):
        tmp = ""
        count = 0
        for y in x.findAll('a'):
            if count > 0:
                tmp += ' & '
                tmp += y.string
                count += 1
            else:
                tmp = y.string
                count += 1
        artist.append(tmp)

song_album = soup.findAll(
    'div', attrs={"class": "songs-list__col songs-list__col--album typography-body"})
album = []
for i in song_album:
    for x in i.findAll('a'):
        album.append(x.string)

print(len(song_titles), len(artist), len(album))
if len(song_titles) == len(artist) == len(album):
    for i in range(0, len(song_titles)):
        print(f"{song_titles[i].string} by {artist[i]} [{album[i]}]")
