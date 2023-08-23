#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-23 18:58:59

import sys
from rich import print
import asyncio

from collections import deque

class AsyncQueue:
    def __init__(self):
        self.q = deque()
        self.lock = asyncio.Lock()

    async def push(self, item):
        async with self.lock:
            self.q.append(item)

    async def pull(self):
        async with self.lock:
            if not self.q:
                return None

            return self.q.popleft()

    async def length(self):
        async with self.lock:
            return len(self.q)



async def main():
    q = AsyncQueue()

    await q.push('message 1')
    await q.push('message 2')

    print(await q.pull(), await q.length())
    print(await q.pull(), await q.length())
    print(await q.pull(), await q.length())


if __name__ == '__main__':
    asyncio.run(main())

