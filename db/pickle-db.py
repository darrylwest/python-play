#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-05 18:49:39

import sys

import pickledb
from rich import print

db = pickledb.load("data/pickledb.json", False)


def getdb():
    return db


def main(args: list) -> None:
    print(f"{args}")
    db.set("my-key", "my-value")

    print(db.get("my-key"))
    keys = db.getall()
    print(f"keys: {keys}, type: {type(keys)}")

    db.dump()


if __name__ == "__main__":
    main(sys.argv[1:])
