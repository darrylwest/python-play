#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-12 16:57:09

import sys
import os
from pathlib import Path

# from rich import print


def main(args: list) -> None:
    cmd = f"just {''.join(args)}"

    print(cmd)
    os.system(cmd)


if __name__ == "__main__":
    main(sys.argv[1:])
