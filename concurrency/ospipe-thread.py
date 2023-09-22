#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-22 17:43:57

import sys
import os
from rich import print
import time
from threading import Thread


def consumer(reader):
    print("[green3]consumer waiting for data.", flush=True)
    data = os.read(reader, 100)
    print("[green3]consumer received:", data)


def producer(writer):
    for n in range(4):
        time.sleep(1)
        print(".", end="", flush=True)

    print("[yellow]Producer sending data.", flush=True)
    os.write(writer, b"hello from the producer!")


def main(args: list) -> None:
    reader, writer = os.pipe()

    cthread = Thread(target=consumer, args=(reader,))
    cthread.start()

    pthread = Thread(target=producer, args=(writer,))
    pthread.start()

    cthread.join()
    pthread.join()

    os.close(reader)
    os.close(writer)


if __name__ == "__main__":
    main(sys.argv[1:])
