#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-06-11 15:33:29

from pathlib import Path


def main():
    print("one liner...")
    data = [line.strip() for line in open("data/xy.data", "r")]
    print(data)


if __name__ == "__main__":
    main()
