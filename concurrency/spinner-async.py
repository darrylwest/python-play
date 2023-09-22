#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-22 19:13:20

import sys
from rich import inspect
import itertools
import asyncio

async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break

    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='', flush=True)

async def slow() -> int:
    await asyncio.sleep(3)
    return 42

async def supervisor() -> int:
    msg = 'working!'
    spinner = asyncio.create_task(spin(msg))
    inspect(f'spinner object: {spinner}')
    result = await slow()
    spinner.cancel()
    print(f'\rdone {msg}', flush=True)

    return result

def main(args: list) -> None:
    result = asyncio.run(supervisor())
    print(f'result: {result}')

if __name__ == '__main__':
    main(sys.argv[1:])

