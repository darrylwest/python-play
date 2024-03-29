#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-20 16:34:17

from enum import Enum


class Color(Enum):
    RED = "#FF0000"
    GREEN = "#00FF00"
    BLUE = "#0000FF"


def decode_color(colr: str) -> str:
    return Color[colr.upper()].value


if __name__ == "__main__":
    colors = ["red", "green", "blue"]
    values = list(map(decode_color, colors))

    print(f"{colors} = {values}")
