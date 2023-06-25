#!/usr/bin/env python3
# dpw@tiburon.localdomain
# 2023-06-25 14:06:03

import numpy as np

a = 0
b = np.pi
n = 11
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = np.sin(x)

I_riemannL = h * sum(f[:n-1])
err_riemannL = 2 - I_riemannL

I_riemannR = h * sum(f[1::])
err_riemannR = 2 - I_riemannR

I_mid = h * sum(np.sin((x[:n-1] \
        + x[1:])/2))
err_mid = 2 - I_mid

print(f"from UC Berkeley https://pythonnumericalmethods.berkeley.edu/notebooks/chapter21.02-Riemanns-Integral.html")
print(f'\ncalculate the area under the curve of sin(x) between 0 and pi')

print(I_riemannL)
print(err_riemannL)

print(I_riemannR)
print(err_riemannR)

print(f"approximate value: {I_mid} and error {err_mid}")

