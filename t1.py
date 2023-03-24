#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-03-11 22:35:43
#
import numpy as np
import sympy as sym
import math

def a(x):
    return -5*x / (8*x + 7)

def b(x):
    return 6*x**3 / (3*x + 1)

def g(x):
    return (-48*x**4 - 42*x**3 - 15*x**2 - 5*x) / ((8*x + 7)*(3*x + 1))

def f(x):
    r1 = a(x)-b(x)
    r2 = g(x) 

    return r1 - r2

if __name__ == "__main__":
    x = np.linspace(-30, 30, 300)
    y = f(x)

    # show any errors
    z = y[(abs(y) > 0.00005)]

    print(f'{z = }')

