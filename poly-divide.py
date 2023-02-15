#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-15 21:04:51
#
import numpy as np
import sympy as sym
import math

x,y = sym.symbols('x y')


p1 = 4*x**5 - x
p2 = 2*x**3 - x

print(p1, '/', p2)
print('')

print(sym.expand(p1 / p2))
print('')

print(sym.simplify(p1 / p2))

