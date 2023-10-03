#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-28 12:56:14

import sys
import time

import schedule
from rich import print


def job(num: int):
    print(f"i am working on job #{num}")


def config():
    schedule.every(10).seconds.do(job, num=1)
    schedule.every(10).seconds.do(job, num=2)
    schedule.every(20).seconds.do(job, num=3)


def main(args: list) -> None:
    print(f"{args}")

    config()

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main(sys.argv[1:])
