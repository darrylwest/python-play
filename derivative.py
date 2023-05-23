#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-05-02 19:07:03
#
import numpy as np
import sympy as sym

sym.init_printing()

x = sym.symbols('x')

fx = 7**(x**2 - x)
fp = sym.diff(fx)

print(fx, " = ", fp)
