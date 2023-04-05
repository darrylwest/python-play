#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-04-05 13:05:59
#
import numpy as np
import sympy as sym
import math

def foo(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)


foo(42, 2,3,4, foo='bar')
foo(43, 6,4, slober='flarb')

