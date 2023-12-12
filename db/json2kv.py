#!/usr/bin/env python3
# dpw@tiburon.local
# 2023-12-11 22:07:21

import sys
from rich import print
import json
from pathlib import Path

def read_users():
    path = Path("db/user-list.json")
    with path.open(mode="r", encoding="utf-8") as file:
        content = file.read()

    users = json.loads(content)

    return users

def main(args: list) -> None:
    users = read_users()
    n = 100
    # path = Path("/tmp/users.kv")
    for user in users:
        print(f"u{n}", user['email'])
        n += 1
            
if __name__ == '__main__':
    main(sys.argv[1:])
