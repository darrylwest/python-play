#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-09 22:35:13

import asyncio
import sys
import time
from pathlib import Path
from typing import Callable

from httpx import AsyncClient
from rich import print

POP20_CC = ("CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR").split()
BASE_URL = "https://www.fluentpython.com/data/flags"
DEST_DIR = Path("downloaded")


def save_flag(img: bytes, filename: str) -> None:
    (DEST_DIR / filename).write_bytes(img)


def download_all(cc_list: list[str]) -> int:
    return asyncio.run(supervisor(cc_list))


async def get_flag(client: AsyncClient, cc: str) -> bytes:
    url = f"{BASE_URL}/{cc}/{cc}.gif".lower()
    resp = await client.get(url, timeout=6.1, follow_redirects=True)

    return resp.read()


async def download(client: AsyncClient, cc: str):
    image = await get_flag(client, cc)
    save_flag(image, f"{cc}.gif")
    print(cc, end=" ", flush=True)

    return cc


async def supervisor(cc_list: list[str]) -> int:
    async with AsyncClient() as client:
        to_do = [download(client, cc) for cc in sorted(cc_list)]
        res = await asyncio.gather(*to_do)

    return len(res)


def main(downloader: Callable[[list[str]], int]) -> None:
    DEST_DIR.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    count = downloader(POP20_CC)
    elapsed = time.perf_counter() - t0
    print(f"\n{count} downloads in {elapsed:.2f}s")


if __name__ == "__main__":
    main(download_all)
