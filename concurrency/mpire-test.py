#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-12 21:22:23

import sys
import time

from mpire import WorkerPool
from rich import print


def time_consuming_fn(x):
    time.sleep(1)
    return x


def main(args: list) -> None:
    # print(f'{args}')

    t0 = time.time_ns()

    # results = [time_consuming_fn(x) for x in range(10)]
    with WorkerPool(n_jobs=10) as pool:
        results = pool.map(time_consuming_fn, range(20), progress_bar=True)
        # insights = pool.get_insights()

    t1 = time.time_ns()
    print(results)

    # print(insights)

    print(f"elapsed: {(t1 - t0)/1_000_000_000} seconds")


if __name__ == "__main__":
    main(sys.argv[1:])
