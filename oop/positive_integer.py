#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-18 16:48:48


import sys
from rich import print, inspect
from json_mixin import JsonMixin


class PositiveInteger:
    """A descriptor instance for positive integers."""
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        value = instance.__dict__[self._name]
        print(f"[green3]Return value: {value}")
        return value

    def __set__(self, instance, value):
        print(f"[green3]Set the value: {value}")
        if not isinstance(value, int) or value < 0:
            raise ValueError("Positive integer required")

        instance.__dict__[self._name] = value


class Ellipse(JsonMixin):
    width = PositiveInteger()
    height = PositiveInteger()

    def __init__(self, width, height):
        self.width = width
        self.height = height

def create_shape():
    return Ellipse(250, 350)

def main(args: list) -> None:
    print(f'{args}')
    ellipse = Ellipse(25, 35)
    inspect(ellipse)
    print(ellipse.to_json())

if __name__ == '__main__':
    main(sys.argv[1:])

