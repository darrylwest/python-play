#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-15 23:22:29

import typer

from rich.console import Console
console = Console()

DEFAULT_LIMIT = 3

def retry_task(func, limit: int = DEFAULT_LIMIT):
    def wrapper(*args, **kwargs):
        for _ in range(limit):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                console.log(f"exception: {e}")

    return wrapper

@retry_task
def task_runner():
    console.log("run this")
    raise Exception("bad data")


def main() -> None:
    limit = 3
    console.log(f"task retry, {limit=}")

    task_runner()


if __name__ == "__main__":
    typer.run(main)
