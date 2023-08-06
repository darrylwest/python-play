#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-06 16:17:34

import numpy as np

def fn(x):
    return (x**4 + 2*x ** -2) / 8

def calc(x1, x0):
    y1, y0 = (fn(x1), fn(x0))

    xy = (x1 - x0)**2 + (y1 - y0)**2

    return np.sqrt(xy)

def calc_length():
    x = 1.0
    length = 0.0
    dx = 0.001
    x1 = x + dx

    while (x1 <= 2):
        length += calc(x1, x)

        # print(f'{x}, {length}')

        x = x1
        x1 = x + dx

    return length

if __name__ == '__main__':
    chord = calc_length()
    print(f'length: {chord}')
