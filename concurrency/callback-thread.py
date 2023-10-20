#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-19 13:14:43

import sys
import threading

from rich.console import Console

console = Console()


def wait_and_print(msg):
    def callback():
        console.log(msg)
        console.log("done")

    timer = threading.Timer(1.0, callback)
    console.log("start")
    timer.start()


def main(args: list) -> None:
    wait_and_print(f"this is a test: {args}")
    console.log("working")


if __name__ == "__main__":
    main(sys.argv[1:])
