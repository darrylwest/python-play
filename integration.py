#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-23 16:52:45

from math import acos, asin, atan, cos, degrees, radians, sin, tan

import begin
from scipy.constants import e, pi
from scipy.integrate import fixed_quad, quad, quadrature, romberg


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
