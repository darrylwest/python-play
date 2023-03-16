#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-03-14 15:49:58
#

import numpy as np
# import sympy as sym
# import math

def f(x, y):
    # return (8*x**2 * y) + (12*x * y**2)
    return (4*x**4 * y) - (8*x**3 * y) - (2*x**2)

def g(x, y):
    # return (4 * x * y) * (2*x + 3*y)
    return (4*x**4 * y) - (8*x**3 * y) - (2*x**2)

def match(y1, y2):
    return abs(y2 - y1) < 0.000001

xin = np.linspace(-10, 10, 500)
y1out = f(xin, xin+1)
y2out = g(xin, xin+1)

# print(xin)
# print(y1out)
# print(y2out)

results = match(y1out, y2out)
print(f'ok = {results[results != True]}')

