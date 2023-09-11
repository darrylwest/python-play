#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-01 18:59:11

import sys
from rich import print

sys.path.append("/functional")

from scientists import create_list


def main(args: list) -> None:
    print(f"{args}")
    ss = create_list()
    print(ss)


if __name__ == "__main__":
    main(sys.argv[1:])
