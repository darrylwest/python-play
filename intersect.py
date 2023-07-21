#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-12 22:04:42

import begin
import math

def func1(x):
    return 6 / x

def func2(x):
    return 7 - x

def find_intersection(fn1, fn2, startx, endx):
    step = 0.0000001
    tol =  0.000001

    print(f'startx = {startx}')

    x = startx
    while x < endx:
        y1 = fn1(x)
        y2 = fn2(x)
        diff = y2 - y1

        # print(y1,y2,diff)

        if abs(diff) < tol:
            break

        x = x + step

    return x

@begin.start
def main(arg1 = None):
    x = find_intersection(func1, func2, 5.9, 6.1)
    print(x)
