import requests
from .KeyParser import KeyDataParser

def searchKey(keywords):
    keyword = ""
    for word in keywords:
        keyword = keyword + word + "+"

    res = requests.get("https://keytube.net/search/?word=" + keyword[:-1])
    parser = KeyDataParser()
    parser.feed(res.text)
    res = []
    for i in range(len(parser.key_array)):
        res.append({
            "song" : parser.song_array[i],
            "artist" : parser.artist_array[i],
            "key" : parser.key_array[i],
        })

    return res
