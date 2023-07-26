#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-05-18 17:06:49
#

import time
from functools import lru_cache

def fib1(n):
    """
    Return the fibonacci sequence for the specified value of n without recursion
    """
    f0, f1 = 0, 1

    f = [1] * n

    for i in range(1, n):
        f[i] = f0 + f1
        f0, f1 = f1, f[i]

    return f[-1]


def test_fib1(n):
    start_time = time.perf_counter()
    v = fib1(n)
    end_time = time.perf_counter()

    print(f"{v}, fib1 exec time: {end_time - start_time}")


def fib2(n):
    return n if n < 2 else fib2(n - 1) + fib2(n - 2)

def test_fib2(n):
    start_time = time.perf_counter()
    v = fib2(n)
    end_time = time.perf_counter()

    print(f"{v}, fib2 exec time: {end_time - start_time}")

@lru_cache(maxsize=None)
def fib3(n):
    return n if n < 2 else fib3(n - 1) + fib3(n - 2)

def test_fib3(n):
    start_time = time.perf_counter()
    v = fib3(n)
    end_time = time.perf_counter()

    print(f"{v}, fib3 exec time: {end_time - start_time}")

test_n = 50

test_fib1(test_n)
# test_fib2(test_n)
test_fib3(test_n)
