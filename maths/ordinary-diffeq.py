#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-03 22:16:20
#

import matplotlib.pyplot as plt
import numpy as np

# Define parameters
f = lambda t, s: np.exp(-t)  # ODE
h = 0.01  # Step size
t = np.arange(0, 1 + h, h)  # Numerical grid
s0 = -1  # Initial Condition

# Explicit Euler Method
s = np.zeros(len(t))
s[0] = s0

for i in range(0, len(t) - 1):
    s[i + 1] = s[i] + h * f(t[i], s[i])

plt.figure(figsize=(12, 8))
plt.plot(t, s, "bo--", label="Approximate")
plt.plot(t, -np.exp(-t), "g", label="Exact")
plt.title(
    "Approximate and Exact Solution \
for Simple ODE"
)
plt.xlabel("t")
plt.ylabel("f(t)")
plt.grid()
plt.legend(loc="lower right")
plt.show()
