#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-04-05 13:05:59
#
import math

import numpy as np
import sympy as sym


def foo(x, *args, **kwargs):
    print(f"x = {x}")
    if x != 40:
        print(args)
        print(kwargs)

    print("-------------")

    return x + 1


n = 40
n = foo(n)
n = foo(n, 2, 3, 4, foo="bar")
n = foo(n, 6, 4, slober="flarb")

print(f"n = {n}")
