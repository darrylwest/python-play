#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-04 16:00:45

import sys
from datetime import datetime, timezone

date_strings = [
    "2023/12/02T05:09:00",
    "2023/12/03T06:09:01",
    "2023/12/04T11:02:02",
    "2023/12/05T07:10:03",
    "2023/12/06T00:08:04",
    "2023/12/07T01:09:05",
    "2023/12/08T02:09:06",
    "2023/12/09T04:09:07",
    "2023/12/10T10:03:08",
    "2023/12/11T08:09:09",
    "2023/12/12T09:06:10",
    "2023/12/13T13:02:20",
    "2023/12/14T14:02:30",
]


def run():
    for ts in date_strings:
        dt = datetime.strptime(ts, "%Y/%m/%dT%H:%M:%S")
        print(ts, "->", dt, dt.toordinal(), dt.isoformat(timespec="microseconds"))


def show_now():
    now = datetime.now(tz=timezone.utc)
    print(f"now: {now} -> {now.isoformat()}")


def main(args: list):
    print(
        "Python : https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime"
    )
    print(
        "Convert the iso8601-ish date strings to datetime; report the date/time, ordinal, and iso output...\n"
    )

    show_now()
    run()
    show_now()


if __name__ == "__main__":
    main(sys.argv[1:])
