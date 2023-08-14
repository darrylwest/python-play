#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-05 23:55:30

import begin
from functools import lru_cache
import time


@lru_cache
def foo(x: int, y: int) -> int:
    """this function uses lru cache to speed operations"""
    print(f"executing foo with x: {x} y: {y}")
    return x**y


@begin.start
def main(arg1=None):
    print(f"foo: {foo.__doc__}")
    for _ in range(20):
        t0 = time.time_ns()
        r = foo(3, 4)
        t1 = time.time_ns()
        print(f"r: {r} {t1-t0}")
