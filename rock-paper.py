#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-03-11 14:55:57
#

# @see enum reference: https://docs.python.org/3/library/enum.html 

from enum import Enum

class ShapePoints(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def points_per_shape(shape: str) -> int:
    return ShapePoints[shape].value

for s in ['ROCK', 'PAPER', 'SCISSORS']:
    print(f'Value: {s}, points: {points_per_shape(s)}')

