#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-05-19 18:52:43
#


def frx(x):
    return 1 / (1 - x)


def taylor(x):
    return [x**n for n in range(200)]


value = 0.8
results = taylor(value)

print(frx(value), "estimate:", sum(results))
print(results[:10])
