import os
import traceback
import uuid
import datetime
import psycopg2
from .ShareMusicFIeld import convertShareMusicDict
from .date import convertDateToString


def getShareMusic():
    connect = psycopg2.connect(
        "host=" + os.getenv('DBHOST') + " " +
        "password=" + os.getenv('DBPASS') + " " +
        "dbname=" + "karaoke" + " " +
        "user=" + os.getenv('DBUSER') + " "
    )
    cur = connect.cursor()

    cur.execute("SELECT * FROM share_musics")
    records = cur.fetchall()
    return convertShareMusicDict(records)


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
        cur.execute("INSERT INTO share_musics VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
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

        cur.execute("DELETE FROM share_musics WHERE id = '" + id + "'")
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
                    UPDATE share_musics
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
