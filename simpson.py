#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-20 21:20:47

import begin
from dataclasses import dataclass
from collections.abc import Callable
import numpy as np
# from scipy import integrate

"""
Create a SimplsonsRule class 

create a funcion to process the equation

def fn(x): y

sr = SimpsonsRule(fn, *start, *stop, *intervals, *error_budget, *show_error)

"""

@dataclass
class SimpsonsData:
    a: float = 0.0
    b: float = 1.0
    n: int = 10
    dx: float = 1.0


def my_func(x):
    return np.sin(x)

def calc_intervals(sr: SimpsonsData):
    stack = []
    x = sr.a
    while x <= sr.b:
        v = sr.func(x)
        print(f'{x} {v}')
        stack.append(v)

        x += sr.dx

    return stack

def process_list(lst):
    acc = lst[0] + lst[-1]
    for idx, n in enumerate(lst[1:-1]):
        print(idx, n)

    result = acc * (np.pi / 10 / 3)
    print(result)
    return result

@begin.start
def main(arg1 = None):

    count = 10
    data = SimpsonsData(0, np.pi, count, np.pi/count)
    print(data)

    stack = calc_intervals(data)
    print(f"list size: {len(stack)}")
    process_list(stack)

    
