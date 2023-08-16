#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-16 13:42:45

import typer
from rich import print

import sqlite3
from contextlib import closing

def connect(path):
    conn = sqlite3.connect(path)
    return conn

def query(conn, query):
    cursor = conn.cursor()
    rows = cursor.execute(query).fetchall()

    return rows

def main(dbpath: str) -> None:
    # path = "db/user.db"
    with closing(connect(dbpath)) as conn:
        rows = query(conn, "select * from user")
        print(rows)


if __name__ == '__main__':
    typer.run(main)

