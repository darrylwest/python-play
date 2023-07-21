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

"""

@dataclass
class SimpsonsData:
    a: float = 0.0
    b: float = 1.0
    n: int = 10
    dx: float = 1.0


class SimpsonsCalculator():
    def __init__(self, ctx: SimpsonsData):
        self.ctx = ctx
        print(ctx)

def my_func(x):
    return np.sin(x)

def calc_intervals(ctx: SimpsonsData):
    stack = []
    x = ctx.a
    while x <= ctx.b:
        v = my_func(x)
        print(f'{x} {v}')

        stack.append(v)

        x += ctx.dx

    return stack

def process_list(lst):
    acc = lst[0] + lst[-1]
    for idx, v in enumerate(lst[1:-1]):
        if idx % 2 == 0:
            acc += 4 * v
        else:
            acc += 2 * v

        print(idx, v, acc)

    result = acc * (np.pi / 10 / 3)

    print(f"sum: {result}")

    return result

@begin.start
def main(arg1 = None):

    count = 10
    ctx = SimpsonsData(0, np.pi, count, np.pi/count)
    calc = SimpsonsCalculator(ctx)
    print(calc)


    stack = calc_intervals(ctx)
    print(f"list size: {len(stack)}")
    process_list(stack)

    
