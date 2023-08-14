#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-21 20:56:11

import asyncio
import datetime


async def loop():
    while True:
        nxt = asyncio.sleep(2)

        print(f"this is my job: {datetime.datetime.now()}")

        await nxt


if __name__ == "__main__":
    asyncio.run(loop())
