#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-09 23:24:37

import sys
from rich import print
import asyncio


async def main(args: list) -> None:
    if args:
        cmd = ' '.join(args)
    else:
        cmd = 'lsd -l data/'

    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')

    if stdout:
        print(f'[stdout]\n{stdout.decode()}')

    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

if __name__ == '__main__':
    asyncio.run(main(sys.argv[1:]))

