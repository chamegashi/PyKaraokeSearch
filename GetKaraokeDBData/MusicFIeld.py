from typing import List, Literal


"""
    入力順

    (1, 'ANIMA', 'あにま', 'ReoNa', -3, 'hiC', '90.000', 'massann')
    id, title, hiragana, artist, key, max_key, max_score, user_id  
"""


def convertMusicDict(musicArray: List):
    retArray = []
    for music in musicArray:
        retArray.append({
            "id": music[0],
            "music_name": music[1],
            "music_name_hira": music[2],
            "artist": music[3],
            "key": music[4],
            "max_key": music[5],
            "max_score": music[6],
            "user_id": music[7],
        })

    return retArray
