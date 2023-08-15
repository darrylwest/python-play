#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-24 16:14:50

import begin
import sympy as sym


# indefinite integral of a linear rational equation
def rational_test():
    x = sym.Symbol("x")

    y = 1 / (x**3 + x)
    v = sym.integrate(y, x)

    print(v)


# definite integral of a 3rd order polynomial
def cubed_test():
    (a, b) = (-1, 1)
    x = sym.Symbol("x")
    y = x**3 + 5

    v = sym.integrate(y, (x, a, b))
    print(f"{y} = {v}")


@begin.start
def main(arg1=None):
    # cubed_test()
    rational_test()
