#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-07 14:58:16
#

from math import sqrt

def Prime(number,itr): #prime function to check given number prime or not
    if itr == 1: #base condition
        return True
    if number % itr == 0: #if given number divided by itr or not
        return False
    if Prime(number,itr-1) == False: #Recursive function Call
        return False
        
    return True

for num in range(10000, 101000):
    itr = int(sqrt(num)+1)

    p = Prime(num, itr)
    if p:
        print(num, "is prime:", p)


