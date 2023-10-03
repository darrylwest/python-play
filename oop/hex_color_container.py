#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-18 22:46:19

import sys

from rich import inspect, print


class HexColorContainer:
    def __init__(self, *args):
        self._colors = []
        for arg in args:
            self.add_color(arg[0], arg[1], arg[2])

    def add_color(self, red, green, blue):
        self._colors.append(f"#{red:02x}{green:02x}{blue:02x}")

    def __iter__(self):
        return self._colors.__iter__()

    def __getitem__(self, key):
        return self._colors[key]

    def __len__(self):
        return len(self._colors)


def create_container():
    return HexColorContainer(
        (255, 255, 240),
        (206, 39, 59),
        (205, 30, 159),
        (225, 30, 15),
        (240, 240, 0),
    )


def main(args: list) -> None:
    print(f"{args}")

    container = create_container()
    inspect(container)

    print(f"length: {len(container)}")

    print(container._colors)

    for color in container:
        print(f"[{color}] = {color}")


if __name__ == "__main__":
    main(sys.argv[1:])
