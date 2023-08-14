#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-17 14:32:20

import math

import numpy as np
import sympy as sym

x = sym.symbols("x")

expr = [x * x**2 * 3 * x, (x + 9) * (x - 9), x**2 - 3 * x - 28, 3 * x + 4 > 6]

for i in range(0, len(expr)):
    print(expr[i], sym.simplify(expr[i]), sym.solve(expr[i]))
