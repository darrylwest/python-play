#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-05-15 13:30:40
#
from collections import namedtuple

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

Points = namedtuple('Points', ['x', 'fx'])

def example_1():
    # needs to be an odd number to include zero
    x = np.linspace(-5,5,1001)
    fx = x**2 * np.exp(-x**2)
    points = Points(x, fx)

    return points

def example_2():
    x = np.linspace(-1.6,1.6,1001)
    fx = -x**4 + 3*x**2
    points = Points(x, fx)

    return points

points = example_1()

dfx = np.diff(points.fx) / (points.x[1]-points.x[0])
local_max = find_peaks(points.fx)[0]
local_min = find_peaks(-points.fx)[0]

xmax,ymax = points.x[local_max], points.fx[local_max]
xmin,ymin = points.x[local_min], points.fx[local_min]

plt.plot(points.x, points.fx)
plt.plot(points.x[0:-1],dfx)

plt.plot(xmax, ymax, 'ro')
plt.plot(xmin, ymin, 'ro')
plt.grid()

plt.show()

