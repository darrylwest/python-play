#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-22 17:26:43

import os
import sys
import time

from rich import print


def main(args: list) -> None:
    r, w = os.pipe()

    pid = os.fork()

    if pid:
        os.close(w)

        print("[green3]parent waiting for data.", flush=True)
        data = os.read(r, 100)
        print("[green3]parent received:", data)

        os.close(r)

    else:
        os.close(r)

        for n in range(4):
            time.sleep(1)
            print(".", end="", flush=True)

        print("[yellow]Child sending data.", flush=True)
        os.write(w, b"hello from the child!")
        os.close(w)


if __name__ == "__main__":
    main(sys.argv[1:])
