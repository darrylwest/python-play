#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-30 15:13:28

import sys
import time
from rich import print
from rich.live import Live
from rich.table import Table

def main(args: list) -> None:
    print(f'{args}')

if __name__ == '__main__':
    main(sys.argv[1:])
    table = Table()
    table.add_column("Row ID")
    table.add_column("Description")
    table.add_column("Level")

    with Live(table, refresh_per_second=4) as live:  # update 4 times a second to feel fluid
        for row in range(25):
            live.console.print(f"Working on row #{row}")
            time.sleep(0.4)
            table.add_row(f"{row}", f"description {row}", "[red]ERROR")



