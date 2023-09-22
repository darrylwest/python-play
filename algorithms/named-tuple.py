#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-03-06 14:09:58
#

from collections import namedtuple

print(
    "namedtuple creates an immutable instance with named attributes including function pointers..."
)


# a method to attach to the tuple
def talk():
    return f"My vroooooom!"


def shout(car):
    return f"my {car.color} car!".upper()


Car = namedtuple("Car", "color mileage sound")
Car.shout = shout

fast_car = Car("red", 342, talk)
print(f"My fast car: {fast_car}\nIt goes {fast_car.sound()}")
print(Car.shout(fast_car))


# this throws
# fast_car.color = 'blue'
