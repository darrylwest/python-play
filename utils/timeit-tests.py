#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-18 17:52:46

# ref: https://docs.python.org/3/library/timeit.html

import sys
from timeit import timeit

from rich import print


def main(args: list) -> None:
    # print(f'{args}')

    t1 = timeit('"-".join(str(n) for n in range(100))', number=10000)
    print(f"loop  :{t1}")

    t2 = timeit('"-".join([str(n) for n in range(100)])', number=10000)
    print(f"comp():{t2}")

    t3 = timeit('"-".join(map(str, range(100)))', number=10000)
    print(f"map() :{t3}")


if __name__ == "__main__":
    main(sys.argv[1:])
