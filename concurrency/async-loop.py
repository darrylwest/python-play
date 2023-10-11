#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-21 20:56:11

import asyncio
import datetime


async def loop():
    count = 5
    print(f'will loop {count} times...')
    for n in range(count):
        nxt = asyncio.sleep(2)

        print(f"{n+1}: this is my job: {datetime.datetime.now()}")

        await nxt


if __name__ == "__main__":
    asyncio.run(loop())
