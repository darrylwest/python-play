#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-01 18:57:23

import sys
from collections import namedtuple

from rich import print

Scientist = namedtuple(
    "Scientist",
    [
        "name",
        "field",
        "born",
        "nobel",
    ],
)


def create_list():
    return (
        Scientist(name="Ada Lovelace", field="math", born=1815, nobel=False),
        Scientist(name="Emmy Noether", field="math", born=1882, nobel=False),
        Scientist(name="Marie Curie", field="math", born=1867, nobel=True),
        Scientist(name="Tu Youyou", field="physics", born=1930, nobel=True),
        Scientist(name="Ada Yonath", field="chemistry", born=1939, nobel=True),
        Scientist(name="Vera Rubin", field="chemistry", born=1928, nobel=False),
        Scientist(name="Sally Ride", field="physics", born=1951, nobel=False),
    )


if __name__ == "__main__":
    scientists = create_list()
    print(scientists)
