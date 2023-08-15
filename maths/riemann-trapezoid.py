#!/usr/bin/env python3
# dpw@tiburon.local
# 2023-06-25 15:11:11

import numpy as np

a = 0
b = np.pi
n = 11
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = np.sin(x)

I_trap = (h / 2) * (f[0] + 2 * sum(f[1 : n - 1]) + f[n - 1])
err_trap = 2 - I_trap

print(f"approximate value: {I_trap} and error {err_trap}")
