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
    return 2 * x


def f(x):
    # return x ** 3 - 3 * x +  1
    return x**5 + 8 * x**4 - 2 * x - 7


def f_prime(x):
    # return 3 * x ** 2 - 3
    return 5 * x**4 + 32 * x**3 - 2


def newtons_method(
    x0,  # initial guess
    f,  # pointer to f(x)
    f_prime,  # pointer to f'(x)
    tolerance,  # accuracy desired
    epsilon,  # smallest divisor
    max_iterations,  # max loops
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


zeros = []

tol = 0.0000000000001
guess = 1.5
x = newtons_method(guess, f, f_prime, tol, tol, 20)
y = f(x)
print("Result: ", x, y)
zeros.append(x)

guess = -0.5
x = newtons_method(guess, f, f_prime, tol, tol, 20)
y = f(x)
print("Result: ", x, y)
zeros.append(x)


guess = -7.5
x = newtons_method(guess, f, f_prime, tol, tol, 20)
y = f(x)
print("Result: ", x, y)
zeros.append(x)

print(f"summary: {zeros}")
