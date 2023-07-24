#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-24 18:36:19

import begin
import time

def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

@begin.start
def main(arg1 = None):
    fgen = fib_generator()
    while True:
        print(next(fgen))
        time.sleep(0.3)

