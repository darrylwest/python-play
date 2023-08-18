#!/usr/bin/env python3
# dpw@tiburon.local
# 2023-02-27 18:54:54
#
# @see https://medium.com/python-in-plain-english/yes-you-can-write-switch-statements-in-python-815da93996a


def matchit(n):
    match n:
        case 0:
            return "zero"
        case 1:
            return "one"
        case _ if n % 2 == 0:
            return f"the number {n} is even"
        case _:
            return f"number {n} is odd"


for n in range(10):
    msg = matchit(n)
    print(msg)
