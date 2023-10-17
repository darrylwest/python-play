#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-17 14:58:12

import functools
import sys
from time import sleep


def main(args: list) -> None:
    print(f"{args}")

    unbuffered_print = functools.partial(print, end=" ", flush=True)

    for t in range(10, 0, -1):
        unbuffered_print(t)
        sleep(0.1)

    print("boom!")


if __name__ == "__main__":
    main(sys.argv[1:])
