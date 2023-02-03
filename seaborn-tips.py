#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-03 21:39:21
#

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

graph = sns.FacetGrid(tips, col ="sex", hue ="day")

graph.map(plt.scatter, "total_bill", "tip", edgecolor ="w").add_legend()

plt.show()

