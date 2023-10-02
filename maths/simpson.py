#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-20 21:20:47

import sys
from collections.abc import Callable
from dataclasses import dataclass

import numpy as np

# from scipy import integrate

"""
SimplsonsData class 

pass in a function or lambda  when creating the calculator

TODO: 
    * calc the number of sub-intervals are required for a set error budget
    * calc the error bounds for the given context
    * add flags to pass in parameters, equations, settings

"""


@dataclass
class SimpsonsData:
    a: float = 0.0
    b: float = 1.0
    n: int = 10
    dx: float = 1.0


class SimpsonsCalculator:
    def __init__(self, ctx: SimpsonsData, func: Callable):
        self.ctx = ctx
        self.fn = func

    def __repr__(self):
        return "f{self.__class__.name}:{self.ctx}"

    def process_list(self, lst):
        acc = lst[0] + lst[-1]
        for idx, v in enumerate(lst[1:-1]):
            acc = acc + 4 * v if idx % 2 == 0 else acc + 2 * v

            # print(idx, v, acc)

        result = acc * (self.ctx.dx / 3)

        # print(f"sum: {result}")

        return result

    def calc(self):
        ctx = self.ctx
        stack = []
        x = ctx.a
        while x <= ctx.b:
            v = self.fn(x)

            # print(f'{x} {v}')

            stack.append(v)

            x += ctx.dx

        return self.process_list(stack)


def calc_sin(count: int = 22):
    count = 22
    ctx = SimpsonsData(0, np.pi, count, np.pi / count)
    src = SimpsonsCalculator(ctx, np.sin)
    result = src.calc()

    print(f"{ctx}, result: {result}")


def calc_ee(count: int = 64):
    # see graph https://www.geogebra.org/calculator/c89s3kb6
    ctx = SimpsonsData(0, 4, count, 4 / count)
    src = SimpsonsCalculator(ctx, lambda x: 1 / 2 * (np.e**x + np.e ** (-x)))
    result = src.calc()

    print(f"{ctx}, result: {result}")


def calc_t(count: int = 1000):
    # see graph https://www.geogebra.org/calculator/mfcwj5j6
    ctx = SimpsonsData(-2, 2, count, 4 / count)
    src = SimpsonsCalculator(ctx, lambda t: t**2 - 4)
    result = src.calc()

    print(f"{ctx}, result: {result}")


if __name__ == "__main__":
    args = sys.argv[1:0]

    calc_sin()
    calc_ee()
    calc_t()
