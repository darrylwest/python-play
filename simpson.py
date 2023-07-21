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

    def __repr__(self):
        return ('f{self.__class__.name}:{self.ctx}')

    def func(self, x):
        return np.sin(x)

    def process_list(self, lst):
        acc = lst[0] + lst[-1]
        for idx, v in enumerate(lst[1:-1]):
            if idx % 2 == 0:
                acc += 4 * v
            else:
                acc += 2 * v

            print(idx, v, acc)

        result = acc * (self.ctx.dx / 3)

        # print(f"sum: {result}")

        return result

    def calc(self):
        ctx = self.ctx
        stack = []
        x = ctx.a
        while x <= ctx.b:
            v = self.func(x)

            # print(f'{x} {v}')

            stack.append(v)

            x += ctx.dx

        return self.process_list(stack)


@begin.start
def main(arg1 = None):

    count = 64
    ctx = SimpsonsData(0, np.pi, count, np.pi/count)
    src = SimpsonsCalculator(ctx)
    result = src.calc()

    print(f'Data: {ctx}, result: {result}')

