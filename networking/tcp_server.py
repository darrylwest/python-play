#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-16 21:19:09

import typer
from rich.console import Console

import socket
import threading

console = Console()


def create_socket(port: int = 16000):
    host = socket.gethostbyname(socket.gethostname())

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))

    console.log(f"server bind to {host}:{port}")

    return server


def main() -> None:
    console.log("create the server tcp socket...")
    server = create_socket()
    console.log(f"socket: {server}")
    server.listen()

    while True:
        client, address = server.accept()
        console.log(f"connected to {address}...")
        client.send("Ready".encode("utf-8"))
        break

    server.close()


if __name__ == "__main__":
    typer.run(main)
