#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-14 14:49:46

# BAD! don't use this!  it's retained as a remindar of what not to do

import sys
from rich import print, inspect
import os
import time

pipe_name = "/tmp/stress-pipe"

# Check if the pipe exists, if not, create it
if not os.path.exists(pipe_name):
    print(f"creating the pipe: {pipe_name}", flush=True)
    os.mkfifo(pipe_name)


def wait_loop():
    with open(pipe_name, "r") as pipe:
        print(f"[yellow]Listening for {pipe_name}", flush=True)
        while True:
            message = pipe.readline().strip()

            print(f"type: {type(message)}")
            inspect(message)

            match message:
                case "start":
                    print(f"[yellow]Starting tests at {time.time_ns() / 1_000_000_000}")

                case "stop":
                    print(f"[green3]Exiting on stop...")
                    break

                case other:
                    print(f"[red]Warning: recieved: {message} unrecognized command...")
                    break


def main(args: list) -> None:
    print(f"{args}")
    wait_loop()


if __name__ == "__main__":
    main(sys.argv[1:])
