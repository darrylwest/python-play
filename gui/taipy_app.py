#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-17 22:08:46

# THis is horrible.  do not use

import sys

from rich import inspect
from taipy import Gui

page = """
# First Taipy web application

## Second Line

## Third


"""


def main(args: list) -> None:
    # print(f'{args}')
    Gui(page=page).run()


if __name__ == "__main__":
    main(sys.argv[1:])
