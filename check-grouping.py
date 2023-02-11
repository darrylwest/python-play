#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-11 15:38:16
#

import numpy as np

def func0(x, y, z):
    return 21*x*y - 112*x*z - 84*x**2 + 28*y*z

# gcf = 7
def func1(x, y, z):
    return 7 * (3*x*y - 16*x*z - 12*x**2 + 4*y*z)

def func2(x, y, z):
    return 7 * (y - 4*x) * (4*z + 3*x)

def func3(x, y, z):
    return -7 * (4*x - y) * (4*z + 3*x)

data = np.loadtxt("xyz.data", dtype='int')

def testit(fn1, fn2):
    ok = True
    for i in range(0, len(data)):
        (x, y, z) = data[i]
        print(x, y, z, " = ", fn1(x, y, z), " = ", fn2(x, y, z), fn1(x, y, z) == fn2(x, y, z), ok )

    return ok

print("test ok: ", testit(func0, func2))

