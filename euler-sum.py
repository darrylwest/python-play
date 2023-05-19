#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 06:57:07 2023

@author: dpw

implement a Taylor series about x = 0 to calculate (approximate) the value of e
"""

from sympy import factorial, exp

def f(x, n):
    return float(x**n / factorial(n))

def sum_series(x, *args, **kwargs):
    max_iterations = 20
    result = 0.0
    
    for i in range(max_iterations):
        result += f(x, i)

    return result

result = sum_series(1)

print(result, 'error:', result - float(exp(1)))
