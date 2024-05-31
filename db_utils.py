import sqlite3


def dict_factory(cursor, row):
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


def get_from_db(query, multiple=False):
    con = sqlite3.connect("db.db")
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute(query)
    if multiple:
        res = cur.fetchall()
    else:
        res = cur.fetchone()
    con.close()
    return res


def insert_into_db(query):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    con.close()