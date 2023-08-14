#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-03 20:57:05
#

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


# let's generate x and y, and add some noise into y
x = np.linspace(0, 10, 101)
y = 0.1 * np.exp(0.3 * x) + 0.1 * np.random.random(len(x))

# Let's have a look of the data
plt.figure(figsize=(10, 8))
plt.plot(x, y, "b.")
plt.xlabel("x")
plt.ylabel("y")
# plt.show()

A = np.vstack([x, np.ones(len(x))]).T
beta, log_alpha = np.linalg.lstsq(A, np.log(y), rcond=None)[0]
alpha = np.exp(log_alpha)
print(f"alpha={alpha}, beta={beta}")

# Let's have a look of the data
plt.figure(figsize=(10, 8))
plt.plot(x, y, "b.")
plt.plot(x, alpha * np.exp(beta * x), "r")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
