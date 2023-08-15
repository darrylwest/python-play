#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-10 14:51:10

import typer


class Movie:
    def __init__(self, rating: int):
        if Movie.validate(rating):
            self._rating = rating

    @property
    def rating(self) -> int:
        return self._rating

    @rating.setter
    def rating(self, value: int) -> None:
        if Movie.validate(value) == True:
            self._rating = value

    @staticmethod
    def validate(value: int) -> bool:
        if 0 <= value <= 5:
            return True
        else:
            raise ValueError("rating must be between 1 and 5")


def main(rating: int) -> None:
    batman = Movie(rating)

    print(f"rating: {batman.rating}")

    batman.rating = 1
    print(f"rating: {batman.rating}")

    # this will throw
    # batman.rating = 6.0


if __name__ == "__main__":
    typer.run(main)
