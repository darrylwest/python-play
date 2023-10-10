#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-09 20:12:43

import asyncio
import socket
import sys
from keyword import kwlist

from rich import print

MAX_KEYWORD_LEN = 5


async def probe(domain: str) -> tuple[str, bool]:
    loop = asyncio.get_running_loop()
    try:
        await loop.getaddrinfo(domain, None)
    except socket.gaierror:
        return (domain, False)

    return (domain, True)


async def main() -> None:
    names = (kw for kw in kwlist if len(kw) <= MAX_KEYWORD_LEN)
    domains = (f"{name}.dev".lower() for name in names)
    coros = [probe(domain) for domain in domains]
    for coro in asyncio.as_completed(coros):
        domain, found = await coro
        mark = "+" if found else " "
        print(f"{mark} {domain}")


if __name__ == "__main__":
    asyncio.run(main())
