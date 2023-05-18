#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-05-18 17:06:49
#

def fib(n):
    """
    Return the fibonacci sequence for the specified value of n
    """
    f0, f1 = 0, 1

    f = [1] * n

    for i in range(1, n):
        f[i] = f0 + f1
        f0, f1 = f1, f[i]

    return f


print(fib(25))

