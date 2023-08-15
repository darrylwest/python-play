#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-14 17:38:38

import typer
from rich import print
from rich.console import Console

console = Console()

data = {
    "name": "Rick",
    "age": 42,
    "items": [{"name": "Portal Gun"}, {"name": "Plumbus"}],
    "active": True,
    "affiliation": None,
}


def main():
    console.log("Here's the data")
    print(data)


if __name__ == "__main__":
    typer.run(main)
