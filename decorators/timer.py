#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-03 01:37:23

# see https://medium.com/@mkuhikar/python-decorators-advanced-67420a5b7278 for notes on Decorators

import time

import begin


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__}() runtime: {end_time - start_time} seconds", flush=True)
        return result

    return wrapper


@timer
def myfn(i):
    time.sleep(0.2)
    return "hello " + str(i)


@begin.start
def main(arg1=None):
    print(
        "simulates a long-running function to demonstrate how to create and use a Decorator..."
    )

    for i in range(10):
        myfn(i + 1)
