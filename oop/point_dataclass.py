#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-18 17:38:36

import sys
from rich import print, inspect
from dataclasses import dataclass, astuple

@dataclass
class Point:
    x: int | float
    y: int | float

def main(args: list) -> None:
    print(f'{args}')

    p = Point(5.6, 7.8)
    inspect(p)

    pp = astuple(p)
    inspect(pp)

if __name__ == '__main__':
    main(sys.argv[1:])

