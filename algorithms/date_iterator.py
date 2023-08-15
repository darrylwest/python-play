#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-15 18:21:59

import typer
from rich import print
from datetime import date, timedelta


class DateRangeContainerIterable:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)


def main() -> None:
    sdt = date(2023, 1, 1)
    edt = date(2023, 1, 10)
    print(f"Create a date range container for dates {sdt} and {edt}")

    seq = DateRangeContainerIterable(sdt, edt)

    for dt in seq:
        print(dt)


def test_sequence():
    sdt = date(2023, 1, 1)
    edt = date(2023, 1, 10)

    seq = DateRangeContainerIterable(sdt, edt)
    assert seq
    dates = [dt for dt in seq]
    assert len(dates) == 9


if __name__ == "__main__":
    typer.run(main)
