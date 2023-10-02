#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-01 19:45:39

import sys

from rich import print

sys.path.append("/functional")

from scientists import create_list


def upper_name(sci):
    return tuple([sci.name.upper(), sci.field, sci.born, sci.nobel])


def name_and_age(sci):
    age = 2023 - sci.born
    return (sci.name, age)


def transform(func, sci_list):
    return tuple(map(func, sci_list))


def main(args: list) -> None:
    print(f"{args}")

    print("name and currnet age")
    print(transform(name_and_age, create_list()))

    print("uppercase name ")
    print(transform(upper_name, create_list()))


if __name__ == "__main__":
    main(sys.argv[1:])
