#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-09 13:22:10

import sys
from concurrent import futures
from time import sleep, strftime, time

from rich import print


def display(*args):
    print(strftime("[%H:%M:%S]"), end=" ")
    print(*args)


def loiter(n):
    msg = "{}loiter({}: doing nothing for {}s"
    display(msg.format("\t" * n, n, n))
    sleep(n)
    msg = "{}loiter({}): done."
    display(msg.format("\t" * n, n))
    return n * 10


def main() -> None:
    display("Script starting.")
    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, range(5))
    display("results:", results)
    display("Waiting for individual results:")
    for i, result in enumerate(results):
        display(f"result {i}: {result}")


if __name__ == "__main__":
    main()
