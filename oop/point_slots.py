#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-18 17:13:02

import sys
from rich import print, inspect
from json_mixin import JsonMixin


class Point(JsonMixin):
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


def main(args: list) -> None:
    print(f"{args}")
    point = Point(5, 2)

    inspect(point)

    point.x = 6
    inspect(point)

    print(
        f"[red]The json mixin fails here because there is no dunder-dict: [green3]{point.to_json()}"
    )


if __name__ == "__main__":
    main(sys.argv[1:])
