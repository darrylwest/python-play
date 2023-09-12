#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-04 16:02:25

import sys
from rich import print, inspect
from unittest.mock import Mock
import json
from datetime import datetime

friday = datetime(year=2023, month=1, day=1)
inspect(friday)

datetime = Mock()


def simple_test():
    json = Mock()
    json.dumps({"key": "value"})
    json.dumps({"key1": "value"})
    json.dumps({"key2": "value"})

    inspect(json)

    json.dumps.assert_called()
    json.dumps.called_with({"key": "value"})
    assert json.dumps.call_count == 3


def is_friday():
    today = datetime.today()
    day_of_week = today.weekday()

    print(today, "day of week", day_of_week)

    return day_of_week == 6


def dates():
    print("friday", friday, friday.weekday())

    datetime.today.return_value = friday

    print(is_friday())
    assert is_friday()


def main(args: list) -> None:
    dates()


if __name__ == "__main__":
    main(sys.argv[1:])
