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
            "id": music["id"],
            "title": music["title"],
            "hiragana": music["hiragana"],
            "artist": music["artist"],
            "max_key": music["max_key"],
            "is_available_msy": music["is_available_msy"],
            "is_available_gil": music["is_available_gil"],
            "is_available_fulu": music["is_available_fulu"],
        })

    return retArray
