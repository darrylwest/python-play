#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-05 15:22:54

# ref: https://pyshorteners.readthedocs.io/en/latest/
# TODO: must have a valid set of API keys...

import pyshorteners
import typer


def main(url: str) -> None:
    print(f"url = {url}")


if __name__ == "__main__":
    typer.run(main)
