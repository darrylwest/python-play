#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-11-03 14:01:56

import sys
from datetime import datetime

from rich import print


def calculate_days(date1, date2):
    date_format = "%Y-%m-%d"
    a = datetime.strptime(date1, date_format)
    b = datetime.strptime(date2, date_format)
    delta = b - a
    return delta.days


def main(args: list) -> None:
    # print(f'{args}')
    date1 = "1950-11-03"
    date2 = "2023-11-03"
    print(
        f"The number of days between {date1} and {date2} is {calculate_days(date1, date2)} days."
    )


if __name__ == "__main__":
    main(sys.argv[1:])
