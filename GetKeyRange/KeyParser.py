from html.parser import HTMLParser
import re

class KeyDataParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.found_td_song = True
        self.found_td_artist = True
        self.found_td_key = True
        self.song_array = []
        self.artist_array = []
        self.key_array = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if re.match('td', tag) and 's' in d.get('class', 's'):
            self.found_td_song = True
        if re.match('td', tag) and 'a' in d.get('class', 'a'):
            self.found_td_artist = True
        if re.match('td', tag) and 'm' in d.get('class', 'm'):
            self.found_td_key = True

    def handle_data(self, data):
        if self.found_td_song:
            self.song_array.append(data)
            self.found_td_song = False
        if self.found_td_artist:
            self.artist_array.append(data)
            self.found_td_artist = False
        if self.found_td_key:
            self.key_array.append(data)
            self.found_td_key = False

    def feed(self, content):
        super().feed(content)
        self.song_array = self.song_array[1:]
        self.artist_array = self.artist_array[1:]
        self.key_array = self.key_array[1:]
