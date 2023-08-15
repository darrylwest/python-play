#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-21 19:38:14
#


# @see spec: https://docs.python.org/3.8/library/string.html#formatspec

print("hello {} has {}".format("larry", "5 cats"))


t = "this is the '{}' for my string."

print(t.format("template"))

print("rounding if 1/3rd is possible: {0:.3f}".format(1 / 3))

print("centered padding {:*^40s}".format("flarb"))
print("or number padding {:0>10d}".format(25))

print("table data...")
for i in range(3, 13):
    t = "{:3d} {:4d} {:5d}"
    print(t.format(i, i**2, i**3))


spec = "https://docs.python.org/3.8/library/string.html#formatspec"
print("\nThe format spec at {}".format(spec))
