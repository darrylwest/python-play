#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-07 14:58:16
#

import argparse
import random
from math import sqrt

import gmpy2 as gym


def isprime(number):  # prime function to check given number prime or not
    return gym.is_prime(number)


def find_large_prime():
    n = random.randrange(1000000000, 1000000000000)
    while isprime(n) == False:
        n = n + 1

    return n


parser = argparse.ArgumentParser(
    description="Enter an integer to determine if it is a prime number"
)
parser.add_argument(
    "integers", metavar="N", type=int, nargs="+", help="the integer(s) to check"
)

args = parser.parse_args()

primes = []
for n in args.integers:
    if isprime(n):
        primes.append(n)
    else:
        print(n, "not prime")

print("primes:", primes)

print("large prime:", find_large_prime())
