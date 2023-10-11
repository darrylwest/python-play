#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-25 16:09:39

import asyncio
import os
import random
import sys
from time import time

import redis
from redis import Redis
from rich import inspect, print


async def connect():
    # this has to be set in the current env
    redis_auth = os.getenv("REDISCLI_AUTH")
    redis_port = os.getenv("REDIS_PORT", 6450)

    print(redis_auth, redis_port)

    r = redis.asyncio.client.Redis(
        host="localhost",
        port=redis_port,
        db=0,
        password=redis_auth,
    )

    # inspect(r)

    return r


async def write_pipe(db: Redis, count: int = 100) -> None:
    async with db.pipeline(transaction=True) as pipe:
        for n in range(count):
            key = random.randint(100000, 999999)
            pipe.set(f"{key}", f"my {key} value # {n}")

        resp = await pipe.execute()

    return resp


async def main(args: list) -> None:
    db = await connect()
    print(db)

    size0 = await db.dbsize()
    print(size0)

    start_time = time()
    await write_pipe(db)
    end_time = time()

    print(f"start: {start_time} end: {end_time} = {end_time - start_time}")
    size1 = await db.dbsize()
    print(f"new size: {size1}")

    await db.aclose()


if __name__ == "__main__":
    # read the .env file?
    asyncio.run(main(sys.argv[1:]))
