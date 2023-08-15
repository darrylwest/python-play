#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-25 16:04:27
#

# @see https://docs.python.org/3/library/timeit.html
# If you’re in a scenario where performance is important, then it’s typically best to profile different approaches and listen
# to the data. timeit is a useful library for timing how long it takes chunks of code to run. You can use timeit to compare the
# runtime of map(), for loops, and list comprehensions:

import random
import timeit

print(
    "get time diff between map, comprehension and simpleloop, please wait...",
    flush=True,
)

TAX_RATE = 0.08
txns = [random.randrange(100) for _ in range(100000)]


def get_price(txn):
    return txn * (1 + TAX_RATE)


def get_prices_with_map():
    return list(map(get_price, txns))


def get_prices_with_comprehension():
    return [get_price(txn) for txn in txns]


def get_prices_with_loop():
    prices = []
    for txn in txns:
        prices.append(get_price(txn))
    return prices


r1 = timeit.timeit(get_prices_with_map, number=100)
print("map :", r1, flush=True)

r2 = timeit.timeit(get_prices_with_comprehension, number=100)
print("comp:", r2, flush=True)

r3 = timeit.timeit(get_prices_with_loop, number=100)
print("loop:", r3, flush=True)
