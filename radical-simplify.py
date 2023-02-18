#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-17 14:32:20

import numpy as np
import sympy as sym
import math

x = sym.symbols('x')

expr = math.sqrt(10 * x) * (-4 * math.sqrt(2 * x) + 2*x)

# this doesnt do what I want
print(sym.simplify(expr))

