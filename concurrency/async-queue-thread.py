import asyncio
import threading
from collections import deque


class AsyncDeque:
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
            item = self.q.popleft()
            return item


def worker(q):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    for i in range(1000):
        loop.run_until_complete(q.push(i))


q = AsyncDeque()
threads = [threading.Thread(target=worker, args=(q,)) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(len(q.q))
