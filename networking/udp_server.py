#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-16 21:58:51

import typer
from rich.console import Console

import socket

console = Console()


def create_server(port: int = 16000):
    host = socket.gethostbyname(socket.gethostname())

    console.log(f"server {host} listening on port {port}...")

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message, address = server.recvfrom(1024)

    console.log(f"{address} -> {message.decode()}")


def main() -> None:
    console.log("create the UDP server")
    create_server()


if __name__ == "__main__":
    typer.run(main)
