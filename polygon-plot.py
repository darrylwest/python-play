#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-18 20:40:36
#

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

y1 = np.array([[1,1],[2,3],[3,1]])
p1 = Polygon(y1,facecolor='m',alpha=0.5)
y2 = np.array([[2,0.2],[2.5,4],[3.5,1]])
p2 = Polygon(y2,facecolor='r',alpha=0.5) #,edgecolor='b')
y3 = np.array([[0.2,0.2],[1.5,4.2],[2.5,1]])
p3 = Polygon(y3,facecolor='b',alpha=0.4)

fig,ax = plt.subplots()
ax.add_patch(p3)
ax.add_patch(p2)
ax.add_patch(p1)

ax.set_xlim([0,4.5])
ax.set_ylim([0,4.5])

plt.title('Multi-Polygon Plot',fontsize='large',fontweight='bold',loc='center')
# plt.grid()
plt.axis('off')

plt.show()

