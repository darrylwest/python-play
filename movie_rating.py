#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-10 14:51:10

import typer


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


def main(rating: int) -> None:
    batman = Movie(1)

    print(f"rating: {batman.rating}")

    batman.rating = rating
    print(f"rating: {batman.rating}")

    # this will throw
    # batman.rating = 6.0


if __name__ == "__main__":
    typer.run(main)
