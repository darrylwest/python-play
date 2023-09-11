#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-01 19:58:45

import sys
from rich import print
from functools import reduce

sys.path.append("/functional")
from scientists import create_list


def main(args: list) -> None:
    print(f"{args}")

    year = 2023

    add_age = lambda acc, sci: acc + (year - sci.born)

    tage = reduce(add_age, create_list(), 0)
    print("age sum:", tage)

    # a better way is to use sum around a generator like this
    tage = sum(year - s.born for s in create_list())
    print("sum ages from generator: ", tage)


if __name__ == "__main__":
    main(sys.argv[1:])
