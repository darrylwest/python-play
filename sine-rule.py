#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-04-01 21:30:55
#
import math


# implement two sine rules, angle, side, angle -> side and angle, side, side -> angle (acute)

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

if __name__ == "__main__":
    A, a, B = (58, 14, 75)
    b = sin_rule_asa(A, a, B)

    print(f"{A}, {a}, {B} = {b}") 

    A, a, B = (46, 12, 58)
    b = sin_rule_asa(A, a, B)

    print(f"{A}, {a}, {B} = {b}") 

