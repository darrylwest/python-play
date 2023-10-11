#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-16 13:42:45

# TODO ; create a class wrapper/decorator to connect, create, query, update based on
# 1) routing keys
# 2) version attributes, created at, last updated, version, hash
# 4) status str
# 5) value blob or text

import sqlite3
from contextlib import closing

from rich import print


def connect(path):
    conn = sqlite3.connect(path)
    return conn


def query(conn, query):
    cursor = conn.cursor()
    rows = cursor.execute(query).fetchall()

    return rows


def main():
    path = "db/user.db"
    with closing(connect(path)) as conn:
        rows = query(conn, "select * from user")
        print(rows)


if __name__ == "__main__":
    main()
