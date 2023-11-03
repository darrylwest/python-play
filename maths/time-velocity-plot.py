#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-11-03 19:17:56

import sys

import matplotlib.pyplot as plt
import numpy as np
from rich import print

# Given data
t = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
v = np.array([4, 8, 12, 14, 16, 16, 14, 12, 8, 4, 0, -4, -8])

# Create the plot
plt.plot(t, v)

# Add title and labels
plt.title("Plot of v against t", fontsize=14, fontweight="bold")
plt.xlabel("t seconds")
plt.ylabel("v m/s")

plt.grid(True)
# Show the plot
plt.show()
