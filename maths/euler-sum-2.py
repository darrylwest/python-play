#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-06 18:17:37

import math

import begin


def func(x):
    return sum([x**n / math.factorial(n) for n in range(0, 100)])


@begin.start
def main():
    print(func(3 + 5), func(3) * func(5))
