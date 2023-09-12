#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-12 16:57:09

import sys
import os
from pathlib import Path

from rich import print

def find_runner():
    # read this directory for all regular files
    files = (f.lower() for f in os.listdir() if Path(f).is_file())

    # look for a match
    for file in files:
        match file:
            case "makefile":
                return "make"

            case "justfile":
                return "just"

            case "tasks.py":
                return "invoke"

            case "taskfile.yaml" | "taskfile.yml":
                return 'task'

            case "package.json":
                return "npm run"

    # nothing found so return none
    return None


def main(args: list) -> None:
    runner = find_runner()
    if runner is None:
        print('ERROR! unable to locate target from files')
    else:
        cmd = f"{runner} {''.join(args)}"
        os.system(cmd)


if __name__ == "__main__":
    main(sys.argv[1:])
