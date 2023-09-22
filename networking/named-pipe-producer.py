#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-14 15:20:15

# BAD! don't use named-pipes for this

import os
import sys
from rich import print


# Path to your named pipe
pipe_name = "/tmp/stress-pipe"

# Check if the pipe exists, if not, create it
if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)


def send_message(message):
    # Open the pipe in write mode
    with open(pipe_name, "w") as pipe:
        # Read a line from standard input
        # message = input()

        # Write the message to the pipe
        pipe.write(message + "\n")

        # Flush the pipe to ensure the message is sent
        pipe.flush()


def main(args: list) -> None:
    print(f"{args}")
    send_message("start")


if __name__ == "__main__":
    main(sys.argv[1:])
