#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-18 16:22:49
#

import numpy as np
import sympy as sym
import sympy.plotting as spl
import math

sym.var("x")

y = x**2

p = spl.plot(y, show=False)

p.xlim = [-3, 8]
p.ylim = [0, 50]

p.title = "My Simple Sympy Plot"

p[0].label = "y = x^2"
p[0].line_color = "r"
p.legend = True

p.show()
