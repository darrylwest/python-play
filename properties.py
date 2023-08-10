#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-10 14:51:10

import begin

class Movie:
    def __init__(self, r):
        self._rating = r

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if 0 <= value <= 5:
            self._rating = value
        else:
            raise ValueError("rating must be between 1 and 5")

@begin.start
def main(arg1 = None):
    batman = Movie(2.5)

    print(f'rating: {batman.rating}')

    batman.rating = 4.0
    print(f'rating: {batman.rating}')

    batman.rating = 6.0
