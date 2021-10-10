from typing import Dict, List

def make_joysound_responce(JoySoundContents) -> List[Dict[str, str]]:

    contents = []

    for JContent in JoySoundContents['contentsList']:
        contents.append({
            "artist" : JContent['artistName'],
            "song" : JContent['songName'],
            "songID" : JContent['naviGroupId'],
        })

    return contents