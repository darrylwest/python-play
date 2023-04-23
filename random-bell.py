#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-04-23 13:50:13
#
import numpy as np
import sympy as sym
import math

rng = np.random.default_rng()

# a = rng.normal(size=(2, 4))
# print(a)

for i in range(1,10):
    n = rng.integers(low=0, high=100000000)
    print(f'{n:0<8d} {n:0<7X}')
