#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-13 20:10:44
#

import numpy as np
import sympy as sym
from IPython.display import Math, display

x, y = sym.symbols("x y")

sym.init_printing()

display(sym.Integral(sym.sqrt(1 / x), x))
