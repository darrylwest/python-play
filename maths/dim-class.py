#!/usr/bin/env python3
# dpw@piedmont
# 2023-02-26 00:00:58
#


class PlotDim:
    xmin: -10
    xmax: 10
    ymin: -10
    ymax: 10

    def __init__(self, xmin, xmax, ymin, ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def __repr__(self) -> str:
        return f"{type(self).__name__}(xmin={self.xmin}, xmax={self.xmax}, ymin={self.ymin}, ymax={self.ymax})"


# pdm = PlotDim(-2, 2, -3, 3)

# print(pdm)
