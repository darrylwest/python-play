#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-31 17:03:02

#
# NOTE: this is far from complete!
#

import sys
from rich import print, inspect
import asyncio
import json
import time
import aiohttp

async def worker(name, n, session):
    # change this to a custom endpoint to get around the rate-limit of 1 per minute
    url = 'https://catfact.ninja/fact'
    print(f'worker-{name}, url: {url}')
    response = await session.request(method='GET', url=url)
    # inspect(response)
    value = await response.text()

    print(value)
    assert response.status == 200
    assert response.content_type == 'application/json'
    # now that we have confirmed that this is json, decode it and return the numbers

    return value

async def main() -> None:
    async with aiohttp.ClientSession() as session:
        responses = await asyncio.gather(*( worker(f'w-{i}', n, session) for i, n in enumerate(range(5,15))))
        for response in responses:
            print(response)


if __name__ == '__main__':
    start_time = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start_time

    print(f'ran in {elapsed:0.3} seconds')
