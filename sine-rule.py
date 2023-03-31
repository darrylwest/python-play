#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-03-30 22:33:18
#
import math


#
# sine rule with two angles and a known side
#
def cos_rule_sas(b, A, c):
    angle = math.radians(A)
    a = math.sqrt(b**2 + c**2 - 2*b*c * math.cos(angle))

    return a

if __name__ == "__main__":
    b, A, c = (736, 3, 915)
    print(f"b={b}, A={A}, c={c} = {cos_rule_sas(5, 61, 16)}")

