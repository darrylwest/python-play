#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-08 17:43:25

import tomllib
from rich import inspect
from pathlib import Path


def process():
    path = Path("data/data.toml")
    data = tomllib.loads(path.read_text())

    inspect(data)


if __name__ == "__main__":
    process()
