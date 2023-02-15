#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-07 14:58:16
#

import argparse
import sympy as sym
from math import sqrt
import random

def prime(number): #prime function to check given number prime or not
    p = sym.factorint(number)

    return len(p) == 1

def find_large_prime():
    n = random.randrange(1000000000, 1000000000000)
    while prime(n) == False:
        n = n + 1

    return n

parser = argparse.ArgumentParser(description='Enter an integer to determine if it is a prime number')
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='the integer(s) to check') 

args = parser.parse_args()

primes = []
for n in args.integers:
    if prime(n):
        primes.append(n)
    else:
        print(n, 'not prime')

print('primes:', primes)

print('large prime:', find_large_prime())
