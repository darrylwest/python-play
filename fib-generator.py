#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-24 18:36:19

import time

import begin


def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


@begin.start
def main(arg1=None):
    print("Generates an infinite fib sequence...")
    fgen = fib_generator()
    while True:
        print(next(fgen))
        time.sleep(0.2)
