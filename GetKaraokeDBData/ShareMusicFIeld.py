from typing import List, Literal


"""
    入力順

    (1, 'ANIMA', 'あにま', 'ReoNa', 'hiC', 1, 0, 2)
    id, title, hiragana, artist, max_key, is_available_msy, is_available_gil, is_available_fulu
"""


def convertShareMusicDict(musicArray: List):
    retArray = []
    for music in musicArray:
        retArray.append({
            "id": music[0],
            "title": music[1],
            "hiragana": music[2],
            "artist": music[3],
            "max_key": music[4],
            "is_available_msy": music[5],
            "is_available_gil": music[6],
            "is_available_fulu": music[7],
        })

    return retArray
