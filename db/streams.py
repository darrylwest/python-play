#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-19 22:49:50

import asyncio
import os
import sys

import redis.asyncio as redis
from rich import print


class UserStream:
    """UserStream listener start listening to the latest message."""

    def __init__(self, client=None, name="UserStream", last_id="$"):
        self.client = client
        self.name = name
        self.last_id = last_id
        self.keep_running = True

    async def start(self):
        if self.client is None:
            redis_auth = os.getenv("REDISCLI_AUTH")
            redis_port = os.getenv("REDIS_PORT")

            self.client = redis.Redis(
                host="localhost",
                port=redis_port,
                db=0,
                password=redis_auth,
                protocol=3,
            )

            print("connected...")

        task = asyncio.create_task(self.listen())

        return task

    async def stop(self):
        self.keep_running = False

    async def update(self, key: str, value: str):
        msg = {"key": key, "value": value, "op": "update"}
        resp = await self.xadd(self.name, msg)

        return resp

    async def remove(self, key: str):
        msg = {"key": key, "value": value, "op": "remove"}
        resp = await self.xadd(self.name, mgs)

        return resp

    async def len(self) -> int:
        size = await self.client.xlen(self.name)

        return size

    async def trim(self, maxlen=500) -> int:
        db = self.client

        print(f"trim {self.name} messages to {maxlen}")

        return await db.xtrim(self.name, maxlen=maxlen)

    async def process(self, item) -> bytes:
        id, resp = item

        print(id, resp)
        await asyncio.sleep(0.005)

        return id

    async def listen(self, timeout=5000):
        db = self.client

        print("listening...")
        while self.keep_running:
            ss = {self.name: self.last_id}

            resp = await db.xread(ss, count=10, block=timeout)

            for key in resp.keys():
                jlist = resp.get(key).pop()

                for item in jlist:
                    self.last_id = await self.process(item)

        await db.aclose()


async def run():
    print(f"pid: {os.getpid()}")
    stream = UserStream()
    task = await stream.start()

    await stream.trim(100)

    sz = await stream.len()
    print(f"current length: {sz} messages...")

    # now create an add loop to update, remove, len and trim

    await task


if __name__ == "__main__":
    asyncio.run(run())
