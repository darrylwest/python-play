#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-11 15:33:29

import numpy as np
import sympy as sym

# import argparse


def main():
    data = [line.strip() for line in open("xy.data", "r")]
    print(data)


if __name__ == "__main__":
    main()
