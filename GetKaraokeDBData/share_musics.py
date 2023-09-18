import os
import traceback
import uuid
import datetime
import psycopg2
import pymysql.cursors

from .ShareMusicFIeld import convertShareMusicDict
from .date import convertDateToString

def makeConnection():
    return pymysql.connect(host=os.getenv('DBHOST'),
                                user=os.getenv('DBUSER'),
                                password=os.getenv('DBPASS'),
                                database='karaoke',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    

def getShareMusic():
    connection = makeConnection()
    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "SELECT * FROM share_musics"
            cursor.execute(sql)

    records = cursor.fetchall()
    print(records)
    return convertShareMusicDict(records)


"""_summary_

music key
id, title, hiragana, artist, key, max_key, is_available_msy, is_available_gil, is_available_fulu
"""


def registerShareMusic(music):
    try:
        connection = makeConnection()
        date = convertDateToString(datetime.datetime.now())
        new_id = str(uuid.uuid4())


        with connection.cursor() as cursor:
            # Create a new record
            cursor.execute("INSERT INTO share_musics VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
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
            
        connection.commit()

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


def updateShareMusic(music):
    try:
        connection = makeConnection()
        date = convertDateToString(datetime.datetime.now())
        
        with connection.cursor() as cursor:
            cursor.execute("""
                    UPDATE share_musics
                        SET title = %s,
                            hiragana = %s,
                            artist = %s,
                            max_key = %s,
                            is_available_msy = %s,
                            is_available_gil = %s,
                            is_available_fulu = %s,
                            modified = %s
                        WHERE id=%s
                    """,
                    (
                        music["title"],
                        music["hiragana"],
                        music["artist"],
                        music["max_key"],
                        music["is_available_msy"],
                        music["is_available_gil"],
                        music["is_available_fulu"],
                        str(date),
                        music["id"],
                    ))

        connection.commit()
        return {"result": music["id"], "message": ""}
    except Exception as e:
        print(traceback.format_exc())
        return {"result": False, "message": "--- update error ---\n" + traceback.format_exc()}


def updateIsAvailable(music):
    try:
        connection = makeConnection()
        date = convertDateToString(datetime.datetime.now())

        with connection.cursor() as cursor:
            cursor.execute("""
                    UPDATE share_musics
                        SET is_available_msy = %s,
                            is_available_gil = %s,
                            is_available_fulu = %s,
                            modified = %s
                        WHERE id=%s
                    """,
                    (
                        music["is_available_msy"],
                        music["is_available_gil"],
                        music["is_available_fulu"],
                        str(date),
                        music["id"],
                    ))

        connection.commit()
        return {"result": music["id"] + "_" + str(date), "message": "success"}
    except Exception as e:
        print(traceback.format_exc())
        return {"result": False, "message": "--- update error ---\n" + traceback.format_exc()}
