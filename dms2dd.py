#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-03-25 22:51:18
#


def dms2dd(d, m, s):
    return d + m / 60 + s / 3600


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Enter an angle in degrees, minutes and seconds"
    )
    parser.add_argument(
        "numbers",
        metavar="degrees, minutes, seconds",
        type=float,
        nargs="+",
        help="the degrees, minutes and seconds of an angle",
    )
    args = parser.parse_args()

    d = args.numbers[0]
    m = args.numbers[1]
    s = args.numbers[2]

    dd = dms2dd(d, m, s)
    print(f"{dd:.3f}")
