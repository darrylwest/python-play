#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-03 22:11:17
#

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumtrapz, trapz

a = 0
b = np.pi
n = 11
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = np.sin(x)

I_trapz = trapz(f, x)
I_trap = (h / 2) * (f[0] + 2 * sum(f[1 : n - 1]) + f[n - 1])

print(I_trapz)
print(I_trap)

x = np.arange(0, np.pi, 0.01)
F_exact = -np.cos(x)
F_approx = cumtrapz(np.sin(x), x)

plt.figure(figsize=(10, 6))
plt.plot(x, F_exact)
plt.plot(x[1::], F_approx)
plt.grid()
plt.tight_layout()
plt.title("$F(x) = \int_0^{x} sin(y) dy$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(["Exact with Offset", "Approx"])
plt.show()
