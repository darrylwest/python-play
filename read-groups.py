#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-03-11 14:17:10
#

# Read lists of integers from a file
# a new group starts after two successive line feeds 
# finally, print the list of groups

# @see https://www.geeksforgeeks.org/python-map-function/ for python map details

with open("ngroups.txt") as f:
    # split input into groups of strings based on empty lines
    groups = f.read().rstrip().split("\n\n")

    # groups now look like this: ['10\n20\n30', '40\n50\n60', '91\n92\n93\n94\n95']
    # three strings with integers separated by new-line chars
    

    # split and the string values in groups and convert to integers
    nums = [list(map(int, (group.split()))) for group in groups]

print(nums)

