#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-11 15:33:29

from pathlib import Path


def withpath():
    print("with path...", flush=True)

    path = Path.cwd() / Path("data") / Path("xy.data")
    with path.open(mode="r", encoding="utf-8") as file:
        content = file.read()

    lines = content.split("\n")
    print(lines)

    print()


def main():
    withpath()


if __name__ == "__main__":
    main()
