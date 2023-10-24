#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-24 20:42:56

import json
import pickle
import sys
from pathlib import Path

from rich import print


def read_users():
    path = Path("db/user-list.json")
    with path.open(mode="r", encoding="utf-8") as file:
        content = file.read()

    users = json.loads(content)

    return users


def main(args: list) -> None:
    # print(f'{args}')
    users = read_users()
    for user in users:
        print(user)

    pusers = pickle.dumps(users, protocol=pickle.HIGHEST_PROTOCOL)
    print(pusers)


if __name__ == "__main__":
    main(sys.argv[1:])
