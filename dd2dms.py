#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-03-25 22:24:33
#


def dd2dms(dd):
    sgn = -1 if dd < 0 else 1

    mnt, sec = divmod(abs(dd) * 3600, 60)
    deg, mnt = divmod(mnt, 60)

    return (int(sgn * deg), int(mnt), sec)


def dms2dd(d, m, s):
    return d + m / 60 + s / 3600


def format_dms(d, m, s):
    return f"{d}.{m}:{s:.3f}"


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Enter an angle in decimal degrees")
    parser.add_argument(
        "numbers",
        metavar="decimal degrees",
        type=float,
        nargs="+",
        help="the decimal degrees of an angle",
    )
    args = parser.parse_args()

    dd = args.numbers[0]

    d, m, s = dd2dms(dd)
    print(f"dd: {dd} == dms: {format_dms(d, m, s)}")
    # print(f"dms: {format_dms(d, m, s)} == dd: {dd:.3f}")
