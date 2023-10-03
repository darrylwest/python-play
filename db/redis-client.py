#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-25 16:09:39

import os
import sys

import redis
from rich import inspect, print


def connect():
    # this has to be set in the current env
    redis_auth = os.getenv("REDISCLI_AUTH")
    redis_port = os.getenv("REDIS_PORT", 6452)

    # print(redis_auth)
    # print(redis_port)

    r = redis.Redis(host="localhost", port=redis_port, db=0)  # protocol=3)
    r.auth(redis_auth)

    return r


def main(args: list) -> None:
    db = connect()
    print(db)

    keys = db.keys("*")
    print(keys)

    value = db.get(b"mykey")
    print(value)


if __name__ == "__main__":
    # read the .env file?
    main(sys.argv[1:])
