#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-14 15:35:13
#

# perfect square trinomial: greene college algebra @ 5:19

import math

# x^2 + 2xy + y^2 = (x + y)^2 
# x^2 - 2xy + y^2 = (x - y)^2 

def check():
    mn = -10
    mx = 10
    ok = True
    for x in range(mn, mx):
        for y in range(mn, mx):
            a1 = fn1(x, y)
            a2 = fn2(x, y)
            if a1 != a2: 
                ok = False

            print(x, y, " = ", a1, a2, ok)

    return ok

print("ok = ", check())
