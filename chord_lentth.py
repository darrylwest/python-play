#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-06 16:17:34

import numpy as np

# def fn(x): return 1/3 * (x ** 2 + 2) ** (3/2)


def calc(x1, x0):
    y1, y0 = (fn(x1), fn(x0))

    xy = (x1 - x0) ** 2 + (y1 - y0) ** 2

    return np.sqrt(xy)


def calc_length(xstart, xend, fn):
    x = xstart
    length = 0.0
    dx = 0.001
    x1 = x + dx

    while x1 <= xend:
        length += calc(x1, x)

        print(f"{x}, {length}")

        x = x1
        x1 = x + dx

    return length


if __name__ == "__main__":
    # fn = lambda x:  1/3 * (x ** 2 + 2) ** (3/2)
    # fn = lambda x:  (x**4 + 3) / (6 * x)
    fn = lambda x: np.log(1 + x**3)
    chord = calc_length(0.0, 5.0, fn)
    print(f"length: {chord}")
