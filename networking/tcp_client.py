#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-16 21:29:58

import typer
from rich.console import Console

import socket
import threading

console = Console()


def connect(port: int = 16000):
    host = socket.gethostbyname(socket.gethostname())

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    console.log(f"server connecting to {host}:{port}")

    client.connect((host, port))

    return client


def main() -> None:
    client = connect()

    for n in range(10):
        client.send("rtkey".encode())
        data = client.recv(1024).decode()
        console.log(f"server-> {data.rstrip()}")

    client.send("bye".encode())
    data = client.recv(1024).decode()
    client.close()


if __name__ == "__main__":
    typer.run(main)
