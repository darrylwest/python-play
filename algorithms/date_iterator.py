#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-15 18:21:59

from datetime import date, timedelta

from rich.console import Console


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
    console = Console()

    sdt = date(2023, 1, 1)
    edt = date(2023, 1, 10)
    console.log(f"Create a date range container for dates {sdt} and {edt}")

    seq = DateRangeContainerIterable(sdt, edt)
    dates = [dt.strftime("%Y-%m-%d") for dt in seq]
    console.log(dates)


def test_sequence():
    sdt = date(2023, 1, 1)
    edt = date(2023, 1, 10)

    seq = DateRangeContainerIterable(sdt, edt)
    assert seq
    dates = [dt for dt in seq]
    assert len(dates) == 9


if __name__ == "__main__":
    main()
