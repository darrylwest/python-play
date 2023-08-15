#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-14 22:30:16

import typer
from rich.console import Console
from rich.table import Table

console = Console()

def main():
    table = Table("Name", "Item")
    table.add_row("dpw", "pop whistle")
    table.add_row("mart", "smart")

    console.print(table)

if __name__ == '__main__':
    typer.run(main)
