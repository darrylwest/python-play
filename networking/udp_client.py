#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-16 22:04:11

import socket

from rich.console import Console

console = Console()


def create_client(port: int = 16000):
    host = socket.gethostbyname(socket.gethostname())

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    console.log(f"send message to {host}:{port}")

    client.sendto("my rxkey is: 123".encode(), (host, port))
    client.close()


def main() -> None:
    console.log("send a message")
    create_client()


if __name__ == "__main__":
    main()
