#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-24 20:23:32

import sys
from rich import print
import time

import asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(say_after(1, 'hello'))
        task2 = tg.create_task(say_after(2, 'world 2'))
        task3 = tg.create_task(say_after(1, 'world 3'))
        task4 = tg.create_task(say_after(1, 'world 4'))
        task5 = tg.create_task(say_after(1, 'world 5'))



if __name__ == '__main__':
    asyncio.run(main())

