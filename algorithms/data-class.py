#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-18 17:58:17

# see https://medium.com/stackademic/python-unleashing-the-magic-6-dataclasses-eb9afbccf129 for more details

from dataclasses import dataclass

from rich import inspect, print


@dataclass
class Point:
    x: float
    y: float


point = Point(1.0, 2.0)

print(point)

point.x = 13.0

print(point)
inspect(point)
