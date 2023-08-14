#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-18 15:58:41
#

import sympy as sym
import math

sym.var("x y")

eq1 = x**3 - 2 * x**2 - 5 * x + 6
eq2 = x**3 - 2 * x**2 - 5 * x + 3

f1 = sym.factor(eq1)
f2 = sym.factor(eq2)
sl1 = sym.solve(eq1)
sl2 = sym.solve(eq2)

print(eq1, "->", f1, sl1)
print(eq2, "->", sl2)
