#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-23 16:52:45

import begin

from scipy.integrate import quad, quadrature, romberg, fixed_quad
from scipy.constants import pi, e
from math import sin, cos, tan, asin, acos, atan, radians, degrees


def run(fn, a, b):
    print(f"quad       = {quad(fn, a, b)}")
    print(f"romberg    = {quad(fn, a, b)}")
    print(f"quadrature = {quadrature(fn, a, b)}")


def ee_test():
    print("\nee test ------------------------------------------------------")

    fn = lambda x: 1 / 2 * (e**x + e ** (-x))
    run(fn, 0, 4)


def sin_test():
    print("\nsine [0,pi/2] test, expect 2.0 -------------------------------")

    print(f"quad    = {quad(sin, 0, pi)}")
    print(f"romberg = {romberg(sin, 0, pi)}")


@begin.start
def main(arg1=None):
    sin_test()
    ee_test()
