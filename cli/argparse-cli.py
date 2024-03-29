#!/usr/bin/env python3
# dpw@BCT-MBP.localdomain
# 2023-04-25 13:09:26
#

# positional_arg1 positional_arg2 -i --int-val 4 -f 3.3 -F --file file_that_exists -a -b -c

import argparse
from collections import namedtuple


def main():
    class Ctx:
        pass

    ctx = Ctx()

    parser = argparse.ArgumentParser(
        description="", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("positional_arg1", help="a string")
    parser.add_argument("positional_arg2", help="a string")
    parser.add_argument("-i", "--int-val", default=4, type=int, help="an int value")
    parser.add_argument("-f", default=3.3, type=float, help="a float value")
    parser.add_argument(
        "-F",
        "--file",
        default="file_that_exists",
        type=argparse.FileType(),
        help="a filename",
    )
    parser.add_argument("-a", action="store_true", help="a flag")
    parser.add_argument("-b", action="store_true", help="b flag")
    parser.add_argument("-c", action="store_true", help="c flag")
    args = parser.parse_args(namespace=ctx)

    print(ctx)

    assert ctx.int_val == args.int_val

    print(args.positional_arg1)
    print(args.positional_arg2)
    print(args.int_val)
    print(args.f)
    print(args.file)
    print(args.a)
    print(args.b)
    print(args.c)


if __name__ == "__main__":
    main()
