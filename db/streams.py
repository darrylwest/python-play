#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-19 22:49:50

import asyncio
import sys

import redis.asyncio as redis
from rich import print


class UserStream:
    """UserStream listener."""

    def __init__(self, client=None, name="ustream", last_id="$"):
        self.client = client
        self.name = name
        self.last_id = last_id
        self.max_length = 500
        self.keep_running = True

    async def start(self):
        if self.client is None:
            redis_auth = "testpw"
            redis_port = 6379

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

    async def process(self, item) -> bytes:
        id, resp = item

        print(id, resp)
        await asyncio.sleep(0.005)

        return id

    async def listen(self, timeout=5000):
        db = self.client

        while self.keep_running:
            ss = {self.name: self.last_id}

            resp = await db.xread(ss, count=10, block=timeout)

            len = 0

            for key in resp.keys():
                len += 1
                print(key)
                jlist = resp.get(key).pop()

                for item in jlist:
                    self.last_id = await self.process(item)

            if len > 0:
                await db.xtrim(self.name, maxlen=self.max_length)

        await db.aclose()


if __name__ == "__main__":
    stream = UserStream()
    asyncio.run(stream.start())
