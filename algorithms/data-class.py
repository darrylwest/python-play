#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-18 17:58:17


from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


point = Point(1.0, 2.0)

print(point)

point.x = 13.0

print(point)
