#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-12 22:04:42

import begin

def func1(x):
    return x**3 - 3*x**2 + 1

def func2(x):
    return (4*x**2)/4 - 4

def find_intersection(fn1, fn2, startx, endx):
    step = 0.0000001
    tol =  0.000001


    print(f'startx = {startx}')

    x = startx
    while x < endx:
        y1 = fn1(x)
        y2 = fn2(x)
        diff = y2 - y1

        if abs(diff) < tol:
            break

        x = x + step

    return x

@begin.start
def main(arg1 = None):
    x = find_intersection(func1, func2, 1.3, 1.4)
    print(x)
