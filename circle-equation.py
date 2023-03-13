#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-03-13 17:39:29
#

import argparse
import numpy as np
import sympy as sym
import math
from collections import namedtuple

parser = argparse.ArgumentParser(description='Enter the circle center and radius as x y r')
parser.add_argument('numbers', metavar='3', type=float, nargs='+', help='the circle center x,y and radius r')

args = parser.parse_args()

Circle = namedtuple('Circle', 'cx cy radius')

circle = Circle(args.numbers[0], args.numbers[1], args.numbers[2])

print(f'{circle.cx = }, {circle.cy = }, radius = {circle.radius}')
