#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-27 13:40:12

from collections import defaultdict


def add_dogs(dd):
    dd["dogs"].append("Fido")
    dd["dogs"].append("HotDog")
    dd["dogs"].append("Lassy")


def add_cats(dd):
    dd["cats"].append("Boxcar")
    dd["cats"].append("Fluffy")
    dd["cats"].append("Whiskers")


if __name__ == "__main__":
    print("creates a short lists of dogs and cats")
    dd = defaultdict(list)

    add_dogs(dd)
    add_cats(dd)

    print(dd)
    print(f"length: {len(dd)}")
