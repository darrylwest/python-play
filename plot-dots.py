#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-16 00:39:57
#
import numpy as np
import sympy as sym
import math
import matplotlib.pyplot as plt

xvals = [3, -3]
yvals = [5, 4]

for idx in range(0, len(xvals)):
    x = xvals[idx]
    y = yvals[idx]

    ch = 'go'
    if x < 0:
        ch = 'ro'

    plt.plot(x, y, ch)

plt.axis([-10,10, -6,6])
plt.grid()

plt.show()

