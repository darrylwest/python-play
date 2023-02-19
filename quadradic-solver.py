#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-19 17:53:39
#

import argparse
import scipy as sym
from numpy.lib.scimath import sqrt

parser = argparse.ArgumentParser(description='Enter three coefficient values to calculate the quadratic roots')
parser.add_argument('numbers', metavar='N', type=float, nargs='+', help='the coefficients a, b, and c') 
args = parser.parse_args()

if len(args.numbers) != 3:
    print("Error: please supply values for a, b and c, e.g., 2 7 5")
else:
    a = args.numbers[0]
    b = args.numbers[1]
    c = args.numbers[2]
    quadp = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    quadn = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

    print('solution for ', args.numbers, 'is:', quadp, ',', quadn)

# plot it out?
