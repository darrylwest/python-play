#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-14 22:20:50

import os

folder = "./"

count = 0

for filename in os.listdir(folder):
    # _, extention = os.path.splitext(filename)
    count += 1

    print(f"{filename}")


print(f"\nTotal file count: {count}")
