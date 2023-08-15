#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-03 20:51:40
#

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

x = np.linspace(0, 1, 101)
y = 1 + x + x * np.random.random(len(x))

A = np.vstack([x, np.ones(len(x))]).T

y = y[:, np.newaxis]

alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)), y)
print(alpha)

# plot results
plt.figure(figsize=(10, 8))
plt.plot(x, y, "b.")
plt.plot(x, alpha[0] * x + alpha[1], "r")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
