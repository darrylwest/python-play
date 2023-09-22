#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-18 16:12:24

import sys
from rich import print, inspect
from json_mixin import JsonMixin


class AirCraft(JsonMixin):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
        self._flying = False

    def takeoff(self):
        print("[green3]Taking flight!")
        self._flying = True

    def land(self):
        print("[red]Landing.")
        self._flying = False


class Plane(AirCraft):
    def __init__(self, make: str, model: str, num_engines: int):
        super().__init__(make, model)
        self.num_engines = num_engines

    def takeoff(self):
        super().takeoff()
        print("[yellow]Gear Up.")

    def land(self):
        super().land()
        print("[yellow]Gear Down.")


def create_piper():
    return Plane("piper", "cub", 2)


def main(args: list) -> None:
    print(f"{args}")
    plane = Plane("Boeing", "727", 2)

    inspect(plane)

    plane.takeoff()
    plane.land()


if __name__ == "__main__":
    main(sys.argv[1:])
