#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-03-12 20:05:01
#

import argparse
import numpy as np
import sympy as sym
import math

parser = argparse.ArgumentParser(description='Enter the line start/end as x1 y1 x2 y2')
parser.add_argument('numbers', metavar='4', type=float, nargs='+', help='the line start/end as x1 y1 x2 y2') 

args = parser.parse_args()

if len(args.numbers) != 4:
    print("Error: please enter the line start and end as x1 y1 x2 y2")
else:
    x1 = args.numbers[0]
    y1 = args.numbers[1]
    x2 = args.numbers[2]
    y2 = args.numbers[3]

    dx, dy = (x2 - x1), (y2-y1)
    llen = math.hypot(dy, dx)

    midx = (x1+x2)/2
    midy = (y1+y2)/2

    m = dy / dx
    b = y1 - (m*x1)
    xi = (y1 - b)/m

    print(f'The midpoint for the line at {x1},{y1} - {x2},{y2} is {midx},{midy}')
    print(f'The slope of the line = {m}, y intercept (b) = {b}, the x intercept is {xi}')
    print(f'The line length is sqrt({dx**2 + dy**2}) = {llen}')

