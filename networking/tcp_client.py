#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-16 21:29:58

import typer
from rich.console import Console

import socket
import threading

console = Console()


def connect(port: int = 14000):
    host = socket.gethostbyname(socket.gethostname())

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    console.log(f"server connecting to {host}:{port}")

    client.connect((host, port))

    return client


def main() -> None:
    client = connect()
    data = client.recv(32).decode()
    console.log(f"server-> {data}")
    client.close()


if __name__ == "__main__":
    typer.run(main)
