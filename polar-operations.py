#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-04-06 20:15:58
#
import math
import cmath as cm
from math import degrees, radians, pi
from cmath import sqrt

def mult_radians(a, b, c, d):
    z1 = cm.rect(a, b)
    z2 = cm.rect(c, d)

    print(z1, z2)

    return z1 * z2

def divide_radians(a, b, c, d):
    z1 = cm.rect(a, b)
    z2 = cm.rect(c, d)

    print(z1, z2)

    return z1 / z2

def mult_degrees(a, b, c, d):
    return mult_radians(a, radians(b), c, radians(d))

def divide_degrees(a, b, c, d):
    return divide_radians(a, radians(b), c, radians(d))

# z3 = mult_radians(8, 4*pi/3, 2, 2*pi/3)
z3 = divide_degrees(20, 140, 4, 35)

print("z3:", round(z3.real,3), round(z3.imag, 3), "j")

modulus = sqrt(z3.real**2 + z3.imag**2).real
phi = degrees(cm.phase(z3))

print("results:", round(modulus, 3), round(phi, 3), "degrees")

