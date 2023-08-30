#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-30 13:10:53

import sys
from rich import print, inspect

import pytest


class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)
    inspect(fruit_salad)

    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)


if __name__ == '__main__':
    print(f"run this with pytest -s {sys.argv[0]}")

