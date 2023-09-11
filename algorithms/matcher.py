#!/usr/bin/env python3
# dpw@tiburon.local
# 2023-02-27 18:54:54
#
# @see https://medium.com/python-in-plain-english/yes-you-can-write-switch-statements-in-python-815da93996a


from rich.console import Console

console = Console()


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


def test_pairs(vars):
    match vars:
        case (0, 0):
            print("got 0,0")
        case (0, b):
            print(f"got 0,{b}")
        case (a, b):
            print(f"got {a},{b}")


if __name__ == "__main__":
    console.rule("find matching combinations in range...")
    for n in range(10):
        msg = matchit(n)
        print(msg)

    console.rule("find matching pairs...")
    mylist = [(0, 0), (0, 5), (2, 6)]
    for tup in mylist:
        test_pairs(tup)
