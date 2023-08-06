#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-05 23:55:30

import begin
from functools import lru_cache

@lru_cache
def foo(x: int, y: int) -> int:
    print(f'executing foo with x: {x} y: {y}')
    return x ** y

@begin.start
def main(arg1 = None):
    for _ in range(10):
        r = foo(3, 4)
        print(f'r: {r}')
