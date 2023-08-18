#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-17 14:36:56

import asyncio
import random


async def show(number: int):
    delay = random.random()
    await asyncio.sleep(delay)

    print(f"{number=}, {delay=}", flush=True)


async def loop():
    for n in range(10):
        await show(n)


if __name__ == "__main__":
    asyncio.run(loop())
