#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-04-20 13:52:41
#
import numpy as np
# import sympy as sym
# import math

def ssum(stop):
    t = 0
    n = 0
    x = 10/11
    
    while n < stop:
        t = t + x**n
        n = n + 1
        
    return t

n = 50
total = ssum(n)

print(n, total)
