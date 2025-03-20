import datetime
import os
import traceback
import psycopg2
from psycopg2.extensions import connection

from utils.convertDateToString import convertDateToString


from .convert_sake_dict import convert_sake_dict


def makeConnection() -> connection:
    return psycopg2.connect(os.getenv("DATABASE_URL"))


def get_sakes():
    connection = makeConnection()
    cur = connection.cursor()

    cur.execute("SELECT * FROM sakes")
    records = cur.fetchall()
    return convert_sake_dict(records)


def delete_sake(id):
    try:
        connection = makeConnection()

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sakes WHERE id = '" + id + "'")

        connection.commit()
        return {"result": id, "message": ""}
    except Exception as e:
        print(traceback.format_exc())
        return {"result": False, "message": "--- delete error ---\n" + traceback.format_exc()}


def update_sake(sake):
    try:
        connection = makeConnection()

        with connection.cursor() as cursor:
            cursor.execute("""
                    UPDATE share_musics
                        SET name = %s,
                            degree = %s,
                            brewery = %s,
                            prefecture = %s,
                            drink_location = %s,
                            image_url = %s,
                            comment = %s,
                            rating = %s,
                            favorite = %s,
                            price = %s,
                            updated = %s
                        WHERE id=%s
                    """,
                           (
                               sake["name"],
                               sake["degree"],
                               sake["brewery"],
                               sake["prefecture"],
                               sake["drink_location"],
                               sake["image_url"],
                               sake["comment"],
                               sake["rating"],
                               sake["favorite"],
                               sake["price"],
                               str(convertDateToString(datetime.datetime.now())),
                           ))

        connection.commit()
        return {"result": sake["id"], "message": ""}
    except Exception as e:
        print(traceback.format_exc())
        return {"result": False, "message": "--- update error ---\n" + traceback.format_exc()}
