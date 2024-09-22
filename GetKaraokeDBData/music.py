import os
import traceback
import uuid
import datetime
import psycopg2
from .MusicFIeld import convertMusicDict
from .date import convertDateToString


def getMusic():
    connect = psycopg2.connect(
        "host=" + os.getenv('DBHOST') + " " +
        "password=" + os.getenv('DBPASS') + " " +
        "dbname=" + "karaoke" + " " +
        "user=" + os.getenv('DBUSER') + " "
    )
    cur = connect.cursor()

    cur.execute("SELECT * FROM musics")
    records = cur.fetchall()
    return convertMusicDict(records)

def getMusicById(music_id):
    connect = psycopg2.connect(
        "host=" + os.getenv('DBHOST') + " " +
        "password=" + os.getenv('DBPASS') + " " +
        "dbname=" + "karaoke" + " " +
        "user=" + os.getenv('DBUSER') + " "
    )
    cur = connect.cursor()

    cur.execute("SELECT * FROM musics WHERE id = %s", (music_id))
    records = cur.fetchall()
    return convertMusicDict(records)

"""_summary_

music key
id, title, hiragana, artist, key, max_key, max_score, user_id
"""


def registMusic(music):
    try:
        connect = psycopg2.connect(
            "host=" + os.getenv('DBHOST') + " " +
            "password=" + os.getenv('DBPASS') + " " +
            "dbname=" + "karaoke" + " " +
            "user=" + os.getenv('DBUSER') + " "
        )
        cur = connect.cursor()

        date = convertDateToString(datetime.datetime.now())
        cur.execute("INSERT INTO musics VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        str(uuid.uuid4()),
                        music["music_name"],
                        music["music_name_hira"],
                        music["artist"],
                        music["key"],
                        music["max_key"],
                        music["max_score"],
                        music["user_id"],
                        str(date),
                        str(date),
                    ))
        connect.commit()
        return {"result": True, "message": ""}
    except Exception as e:
        print(traceback.format_exc())
        return {"result": False, "message": "--- regist error ---\n" + traceback.format_exc()}


"""_summary_

music key
id, title, hiragana, artist, key, max_key, max_score, user_id
"""


def deleteMusic(id):
    try:
        connect = psycopg2.connect(
            "host=" + os.getenv('DBHOST') + " " +
            "password=" + os.getenv('DBPASS') + " " +
            "dbname=" + "karaoke" + " " +
            "user=" + os.getenv('DBUSER') + " "
        )
        cur = connect.cursor()

        cur.execute("DELETE FROM musics WHERE id = '" + id + "'")
        connect.commit()
        return {"result": True, "message": ""}
    except Exception as e:
        print(traceback.format_exc())
        return {"result": False, "message": "--- delete error ---\n" + traceback.format_exc()}


def updateMusic(music):
    try:
        connect = psycopg2.connect(
            "host=" + os.getenv('DBHOST') + " " +
            "password=" + os.getenv('DBPASS') + " " +
            "dbname=" + "karaoke" + " " +
            "user=" + os.getenv('DBUSER') + " "
        )
        cur = connect.cursor()

        date = convertDateToString(datetime.datetime.now())
        cur.execute("""
                    UPDATE musics
                        SET music_name = %s,
                            music_name_hira = %s,
                            artist = %s,
                            key = %s,
                            max_key = %s,
                            max_score = %s,
                            modified = %s
                        WHERE id=%s""",
                    (
                        music["music_name"],
                        music["music_name_hira"],
                        music["artist"],
                        music["key"],
                        music["max_key"],
                        music["max_score"],
                        str(date),
                        music["id"],
                    ))
        connect.commit()
        return {"result": True, "message": ""}
    except Exception as e:
        print(traceback.format_exc())
        return {"result": False, "message": "--- update error ---\n" + traceback.format_exc()}
