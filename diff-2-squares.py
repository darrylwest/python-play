#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-14 14:34:37
#

# product of conjegates

import numpy as np
import sympy as sym
import math

a = 8
b = 50

def fn1(x, y):
    return a*x**10 - b*y**12

# intermediate step
def fn2a(x, y):
    a1 = math.sqrt(a / 2) # to get 2x**5
    b1 = math.sqrt(b / 2) # to get 5x**6
    return 2*( (a1*x**5)**2 - (b1*y**6)**2 )

def fn2(x, y):
    x1 = 2*x**5
    y1 = 5*y**6
    return 2*( (x1 + y1) * (x1 - y1) )

def check():
    mn = -10
    mx = 10
    ok = True
    for x in range(mn, mx):
        for y in range(mn, mx):
            a1 = fn1(x, y)
            a2 = fn2(x, y)
            if a1 != a2: 
                ok = False

            print(x, y, " = ", a1, a2, ok)

    return ok

print("ok = ", check())
