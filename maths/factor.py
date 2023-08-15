#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-05 22:40:03
#

import sympy
from sympy import *

var("x y")

eq = x**3 - 2 * x**2 - 5 * x + 6

f = sympy.factor(eq)
print(eq, " = ", f)
