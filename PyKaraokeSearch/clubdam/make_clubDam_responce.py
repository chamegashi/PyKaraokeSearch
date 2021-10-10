from typing import Dict, List
 
def make_clubDam_responce(damContents) -> List[Dict[str, str]]:

    contents = []

    for DContent in damContents['list']:
        contents.append({
            "artist" : DContent['artist'],
            "song" : DContent['title'],
            "songId" : DContent['requestNo'],
        })

    return contents