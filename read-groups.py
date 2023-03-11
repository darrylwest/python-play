#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-03-11 14:17:10
#

# @see https://www.geeksforgeeks.org/python-map-function/ for python map details

with open("ngroups.txt") as f:
    # split input into groups based on empty lines
    groups = f.read().rstrip().split("\n\n")

    # convert all values in groups to integers
    nums = [list(map(int, (group.split()))) for group in groups]

print(nums)

