#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-03 22:02:01
#

import matplotlib.pyplot as plt
import numpy as np

# step size
h = 0.1
# define grid
x = np.arange(0, 2 * np.pi, h)
# compute function
y = np.cos(x)

# compute vector of forward differences
forward_diff = np.diff(y) / h
# compute corresponding grid
x_diff = x[:-1:]
# compute exact solution
exact_solution = -np.sin(x_diff)

# Plot solution
plt.figure(figsize=(12, 8))
plt.plot(x_diff, forward_diff, "--", label="Finite difference approximation")
plt.plot(x_diff, exact_solution, label="Exact solution")
plt.legend()
plt.show()

# Compute max error between
# numerical derivative and exact solution
max_error = max(abs(exact_solution - forward_diff))
print(max_error)
