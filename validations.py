#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-13 14:40:58


from abc import ABC, abstractmethod
from dataclasses import dataclass


class ValidationBase(ABC):
    @abstractmethod
    def validate(self, value):
        pass


class ValidationDescriptor(ValidationBase):
    def __set_item__(self, owner, name):
        self.storage_name = name

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.storage_name] = value


class PositiveNum(ValidationBase):
    """
    Validate the the number is >= 0
    """

    def validate(self, value):
        if value < 0:
            raise ValueError("Value must be positive")


class MinLenChar:
    """
    Validate that the string character length is >= the minimum
    """

    def __init__(self, length):
        self._length = length

    def validate(self, value):
        if len(value) < self._length:
            raise ValueError(f"Value must be at least {self._length} characters")


class Item:
    """
    A named item with price and quantity
    """

    name = MinLenChar(2)
    price = PositiveNum()
    quantity = PositiveNum()

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f'Item("{self.name}",${self.price},{self.quantity})'


if __name__ == "__main__":
    print(
        """
        Using Python descriptors to create self-validating classes.
        see https://medium.com/python-in-plain-english/a-beginner-guide-into-python-descriptors-4444256f2e54
        Probably better to use the Pydantic V2 module...
    """
    )

    item = Item("Milk", 5.25, 2)
    print(item)

    item.price = 10.0
    item.quantity = 100
    print(item)

    # item.price = -2.0
