#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-02 15:19:11

import sys
from rich import print
import os


def filter_dirs():
    dirs = [d for d in os.listdir(".") if os.path.isdir(d)]

    for d in dirs:
        print(d)


def list_dirs():
    dirs = filter(os.path.isdir, os.listdir("."))

    for d in dirs:
        print(d)


def main(args: list) -> None:
    list_dirs()
    filter_dirs()


if __name__ == "__main__":
    main(sys.argv[1:])
