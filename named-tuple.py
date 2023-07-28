#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-03-06 14:09:58
#

from collections import namedtuple

print('namedtuple creates an immutable instance with named attributes including function pointers...')

def talk():
    return 'vroooooom!'

Car = namedtuple('Car', 'color mileage sound')

fast_car = Car('red', 342, talk)
print(f"My fast car: {fast_car}\nIt goes {fast_car.sound()}")


# this throws
# fast_car.color = 'blue'

