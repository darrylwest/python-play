#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-22 18:31:29

import itertools
import sys
import time
from threading import Event, Thread

from rich import inspect


def spin(msg: str, done: Event) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, end="", flush=True)
        if done.wait(0.1):
            break

    blanks = " " * len(status)
    print(f"\r{blanks}\r", end="", flush=True)


def slow() -> int:
    time.sleep(3)
    return 42


def supervisor() -> int:
    done = Event()
    msg = "working!"
    spinner = Thread(target=spin, args=(msg, done))
    print(f"spinner object: {spinner}")
    spinner.start()
    result = slow()
    done.set()
    print(f"\rdone {msg}", flush=True)

    return result


def main(args: list) -> None:
    result = supervisor()
    print(f"result: {result}")


if __name__ == "__main__":
    main(sys.argv[1:])
