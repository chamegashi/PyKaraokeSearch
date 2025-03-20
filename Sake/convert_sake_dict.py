from typing import List


"""
    入力順

    id, name, degree, brewery, prefecture, drink_location, image_url, comment, rating, favorite, price, created, updated
"""


def convert_sake_dict(sakeArray: List):
    retArray = []
    for sake in sakeArray:
        retArray.append({
            "id": sake[0],
            "name": sake[1],
            "degree": sake[2],
            "brewery": sake[3],
            "prefecture": sake[4],
            "drink_location": sake[5],
            "image_url": sake[6],
            "comment": sake[7],
            "rating": sake[8],
            "favorite": sake[9],
            "price": sake[10],
            "created": sake[11],
            "updated": sake[12]
        })

    return retArray
