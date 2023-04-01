#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-03-30 21:54:35
#
import math

#
# cosine rule with two sides and a known angle between them (in degrees)
#
def cos_rule_sas(b, A, c):
    angle = math.radians(A)
    a = math.sqrt(b**2 + c**2 - 2*b*c * math.cos(angle))

    return a

#
# cosine rule with three sides solve for angle A (opposite of a)
#
def cos_rule_sss(a, b, c):
    radians = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    return math.degrees(radians)


def width_of_orion_belt():
    b, A, c = (736, 3, 915)
    a = cos_rule_sas(b, A, c)
    print(f"Width of Orion's belt from b={b}, A={A}, c={c} = {a}")

    return a

if __name__ == "__main__":
    # a = width_of_orion_belt()
    # print(cos_rule_sss(a, 915, 736))

    b, A, c = (17, 75, 24)
    print(f"b={b}, A={A}, c={c} = {cos_rule_sas(b, A, c)}")

    a, b, c = (15, 60, 50)
    print(f"a={a}, b={b}, c={c} = A = {cos_rule_sss(a, b, c)}")


# TODO: CLI cos-rule --pattern n n n 
# where --pattern = sss or sas


