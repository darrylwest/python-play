#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-05-18 13:28:01
#
import numpy as np
import sympy as sym
# import scipy

def f_sqrt(x):
    return x**2 - 275

def f_sqrt_prime(x):
    return 2*x

def f(x):
    return x ** 3 - 0.1
    # return x**3 - 3*x + 1

def f_prime(x):
    return 3*x ** 2
    # return 3*x**2 - 3 

def newtons_method(
        x0,           # initial guess
        f,            # pointer to f(x)
        f_prime,      # pointer to f'(x)
        tolerance,    # accuracy desired
        epsilon,      # smallest divisor
        max_iterations, # max loops
        ):
    for i in range(max_iterations):
        y = f(x0)

        yprime = f_prime(x0)

        if abs(yprime) < epsilon:
            print("epsilon...")
            break

        x1 = x0 - y / yprime

        print(i, x0, y, yprime, x1)

        if abs(x1 - x0) <= tolerance:
            print("tolerance...")
            return x1

        x0 = x1

    return None

guess = 0.1
tol = 0.0000000000001
x = newtons_method(guess, f, f_prime, tol, tol, 20)
y = f(x)

print("Result: ",x, y)


