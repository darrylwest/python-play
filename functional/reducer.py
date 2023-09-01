#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-01 19:58:45

import sys
from rich import print


def main(args: list) -> None:
    print(f"{args}")


if __name__ == "__main__":
    main(sys.argv[1:])
