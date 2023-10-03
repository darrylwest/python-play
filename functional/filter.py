#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-01 19:23:18

import sys

from rich import print

sys.path.append("/functional")
from scientists import create_list


def with_filter_command():
    print("list of selected records using filter command")
    sci_list = create_list()

    print("list of nobel prize winners as tuples...")
    nobels = tuple(filter(lambda sci: sci.nobel is True, sci_list))
    print(nobels)

    print("list of math people as tuples...")
    maths = tuple(filter(lambda sci: sci.field == "math", sci_list))
    print(maths)

    print("list of math and nobel as tuples...")
    maths_nobel = tuple(
        filter(lambda sci: sci.field == "math" and sci.nobel is True, sci_list)
    )
    print(maths_nobel)


def with_list_comp():
    print("list of selected records using list comprehension")
    sci_list = create_list()

    print("list of nobel prize winners as tuples...")
    nobels = tuple([sci for sci in sci_list if sci.nobel is True])
    print(nobels)

    print("list of math people as tuples...")
    maths = tuple([sci for sci in sci_list if sci.field == "math"])
    print(maths)

    print("list of math and nobel as tuples...")
    maths_nobel = tuple(
        [sci for sci in sci_list if sci.field == "math" and sci.nobel is True]
    )
    print(maths_nobel)


def main(args: list) -> None:
    print(f"{args}")
    with_filter_command()
    with_list_comp()


if __name__ == "__main__":
    main(sys.argv[1:])
