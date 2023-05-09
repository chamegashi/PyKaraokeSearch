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
id, title, hiragana, artist, key, max_key, is_available_msy, is_available_gil, is_available_fulu
"""


def registShareMusic(music):
    try:
        connect = psycopg2.connect(
            "host=" + os.getenv('DBHOST') + " " +
            "password=" + os.getenv('DBPASS') + " " +
            "dbname=" + "karaoke" + " " +
            "user=" + os.getenv('DBUSER') + " "
        )
        cur = connect.cursor()

        date = convertDateToString(datetime.datetime.now())
        new_id = str(uuid.uuid4())
        cur.execute("INSERT INTO share_musics VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        new_id,
                        music["title"],
                        music["hiragana"],
                        music["artist"],
                        music["max_key"],
                        music["is_available_msy"],
                        music["is_available_gil"],
                        music["is_available_fulu"],
                        str(date),
                        str(date),
                    ))
        connect.commit()
        return {"result": new_id, "message": ""}
    except Exception as e:
        print(traceback.format_exc())
        return {"result": False, "message": "--- regist error ---\n" + traceback.format_exc()}


"""_summary_

music key
id, title, hiragana, artist, key, max_key, max_score, user_id
"""


def deleteShareMusic(id):
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
        return {"result": id, "message": ""}
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
        records = cur.fetchall()
        print(records)
        return {"result": True, "message": ""}
    except Exception as e:
        print(traceback.format_exc())
        return {"result": False, "message": "--- update error ---\n" + traceback.format_exc()}


def updateIsAvailable(music):
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
                        SET is_available_msy = %s,
                            is_available_gil = %s,
                            is_available_fulu = %s,
                            modified = %s
                        WHERE id=%s""",
                    (
                        music["is_available_msy"],
                        music["is_available_gil"],
                        music["is_available_fulu"],
                        str(date),
                        music["id"],
                    ))
        connect.commit()
        return {"result": music["id"] + "_" + str(date), "message": "success"}
    except Exception as e:
        print(traceback.format_exc())
        return {"result": False, "message": "--- update error ---\n" + traceback.format_exc()}
