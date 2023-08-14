#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-04-29 14:13:23
#
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from IPython.display import Math, display
from sympy.abc import x

piece1 = x**2
piece2 = -2 * x
piece3 = x**3 / 10

fx = sym.Piecewise((piece1, x < 0), (piece2, (x >= 0) & (x < 3)), (piece3, x >= 3))

fxx = sym.lambdify(x, fx)
xx = np.linspace(-3, 5, 1000)

plt.plot(xx, fxx(xx))
plt.grid()

plt.show()
