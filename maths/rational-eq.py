#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-14 17:54:53
#

# solving rational equations
# 19 / (3*x**2 - 6x) = 1/(3*x) + 2/(x-2)
# refactor to = 0
# 19 / (3*x**2 - 6x) - 1/(3*x) - 2/(x-2) = 0

# LCD = 3x(x - 2)
# factor out

# 1st term: 3x(x - 2) cancels where result = 19
# 2nd: 3x cancels leaving (x - 2)
# 3rd: (x - 2) cancels and we are left with 3x * 2 = 6x


# the original
def f1(x):
    return int(19 / (3 * x**2 - 6 * x) - 1 / (3 * x) - 2 / (x - 2))


# second iteration
def f2a(x):
    return 19 - (x - 2) - 6 * x


def f2b(x):
    return 21 - 7 * x


# 21/7 - x = 0
def f2(x):
    return 21 / 7 - x


def check(x):
    a1 = f1(x)
    a2 = f2(x)
    print("x =", x, "f1(x) =", a1, "f2(x) =", a2, "ok?", a1 == a2)


check(3)
