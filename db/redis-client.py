#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-25 16:09:39

import os
import random
import sys
import time

import redis
from redis import Redis
from rich import inspect, print


def connect():
    # this has to be set in the current env
    redis_auth = os.getenv("REDISCLI_AUTH")
    redis_port = os.getenv("REDIS_PORT", 6452)

    print(redis_auth)
    print(redis_port)

    r = redis.Redis(host="localhost", port=redis_port, db=0)  # protocol=3)
    # r = redis.Redis(host="localhost")
    r.auth(redis_auth)

    return r


def write_pipe(db: Redis, count: int = 10) -> None:
    pipe = db.pipeline()

    for n in range(count):
        key = random.randint(100000, 999999)
        pipe.set(f"{key}", f"my {key} value # {n}")

    pipe.execute()


def main(args: list) -> None:
    db = connect()
    print(db)

    size0 = db.dbsize()
    print(size0)

    start_time = time.time()
    write_pipe(db)
    end_time = time.time()

    print(f"start: {start_time} end: {end_time} = {end_time - start_time}")
    print(f"new size: {db.dbsize()}")


if __name__ == "__main__":
    # read the .env file?
    main(sys.argv[1:])
