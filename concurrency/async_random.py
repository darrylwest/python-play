#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-17 14:36:56

import asyncio
import random
from time import time
from rich import inspect


async def show(number: int):
    delay = random.random() + 2.0
    await asyncio.sleep(delay)

    print(f"{number=}, {delay=}", flush=True)
    return delay


async def loop():
    count = 20
    print(f'\nThis script runs {count} jobs in parallel then awaits for all of them to be completed...\n', flush=True)

    t0 = time()
    jobs = [show(n) for n in range(10)]
    res = await asyncio.gather(*jobs)
    t1 = time()

    # inspect(res)
    print(f'elapsed: {t1-t0}')
    print(f'sum....: {sum(res)}')

if __name__ == "__main__":
    asyncio.run(loop())
