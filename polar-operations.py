#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-04-06 20:15:58
#
import math
import cmath as cm
from math import degrees, radians, pi
from cmath import sqrt

z1 = cm.rect(8, 4*pi/3)
z2 = cm.rect(2, 7*pi/6)

z3 = z1 / z2

print(z1, z2, z3)

modulus = sqrt(z3.real**2 + z3.imag**2).real
phi = degrees(cm.phase(z3))

print("results:", round(modulus, 3), round(phi, 3), "degrees")

