#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-04-01 21:30:55
#
import math


# implement two sine rules, angle, side, angle -> side and angle, side, side -> angle (acute)
# verify with this tool: https://www.omnicalculator.com/math/triangle-angle
# or: https://www.calculatorsoup.com/calculators/geometry-plane/triangle-law-of-sines.php

#
# returns the length of b opposite B
# A = angle in degrees
# a = side opposite A
# B = angle in degrees opposite b
#
def sin_rule_asa(A, a, B):
    aa = math.radians(A)
    ab = math.radians(B)
    return (math.sin(ab) * a) / math.sin(aa)

#
# returns the angle B opposite side b
#
# A = angle in degrees
# a = side opposite A
# b = side opposite B
#
# NOTE: be careful to check if the angle is supposed to be
# acute or obtuse
#
def sin_rule_ass(A, a, b):
    aa = math.radians(A)
    B = math.asin((math.sin(aa) * b)/a)
    return math.degrees(B)

if __name__ == "__main__":
    A, a, B = (58, 14, 75)
    b = sin_rule_asa(A, a, B)

    print(f"{A}, {a}, {B} = {b}") 

    A, a, B = (46, 12, 58)
    b = sin_rule_asa(A, a, B)

    print(f"{A}, {a}, {B} = {b}") 

    A, a, b = (46, 11.92, 14)
    B = sin_rule_ass(A, a, b)
    print(f"{A}, {a}, {b} = {B} degrees") 

    A, a, b = (58, 14, 16)
    B = sin_rule_ass(A, a, b)
    print(f"{A}, {a}, {b} = {B} degrees") 

    A, a, b = (75, 16, 12)
    B = sin_rule_ass(A, a, b)
    print(f"{A}, {a}, {b} = {B} degrees") 

    A, a, b = (30, 19, 37)
    B = sin_rule_ass(A, a, b)
    print(f"{A}, {a}, {b} = {B} degrees, {180-B} obtuse") 

