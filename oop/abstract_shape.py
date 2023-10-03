#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-18 17:51:31

import math
import sys
from abc import ABC, abstractmethod

from rich import inspect, print


class Shape(ABC):
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    @abstractmethod
    def get_area(self):
        pass

    def hex_color(self):
        return f"[red]#{self.red:02x}[green]{self.green:02x}[blue]{self.blue:02x}"


class Circle(Shape):
    def __init__(self, radius: int, red: int, green: int, blue: int):
        self.radius = radius
        super().__init__(red, green, blue)

    def get_area(self):
        return math.pi * pow(self.radius, 2)


def create_circle():
    return Circle(20, 128, 0, 255)


def main(args: list) -> None:
    print(f"{args}")

    circle = create_circle()
    inspect(circle)
    print(circle.hex_color())
    print(f"area: {circle.get_area()}")


if __name__ == "__main__":
    main(sys.argv[1:])
