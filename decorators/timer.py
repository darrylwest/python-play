#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-03 01:37:23

# see https://medium.com/@mkuhikar/python-decorators-advanced-67420a5b7278 for notes on Decorators

from time import time, sleep, monotonic


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = monotonic()
        result = func(*args, **kwargs)
        end_time = monotonic()
        print(f"{func.__name__}() runtime: {end_time - start_time} seconds", flush=True)
        return result

    return wrapper


@timer
def myfn(i, delay):
    sleep(delay)
    return "hello " + str(i)


if __name__ == "__main__":
    delay = 0.2
    print(
        "Simulates a long-running ({delay} seconds), function to demonstrate how to create and use a decorator."
    )

    for i in range(10):
        myfn(i + 1, delay)
