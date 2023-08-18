#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-16 21:19:09

import socket
import subprocess
import threading

import typer
from rich.console import Console

# TODO list
# * switch to file logging, one for the server and one each client (delay until formal project is created)
# * graceful shutdown of clients (will delay until threading is replaced by async)


console = Console()


def create_socket(port: int = 16000):
    host = socket.gethostbyname(socket.gethostname())

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))

    console.log(f"server bind to {host}:{port}")

    return server


def create_key() -> str:
    """return a 16 character routing key"""
    result = subprocess.run("rtkey", capture_output=True, text=True)
    key = result.stdout
    return key[0:16]


def handle_client(client, ipaddr, client_id):
    console.log(f"new connection handled, ip: {ipaddr}, client id: {client_id}")

    # set client timeout
    # recyle the socket after n number of requests?

    try:
        client.send("Ready\n".encode("utf-8"))
        while True:
            data = client.recv(1024)
            if not data:
                break

            message = data.decode("utf-8")
            console.log(f"client ->: {message}")
            if message.startswith("bye"):
                client.send("out\n".encode("utf-8"))
                client.close()
                break

            if message.startswith("rtkey"):
                key = create_key()
                client.send(f"{key}\n".encode("utf-8"))
                continue

            if message.startswith("raise"):
                raise ValueError("boom!")

            client.send("Ok\n".encode("utf-8"))

    except ValueError as err:
        print(err)

    finally:
        client.close()


def main() -> None:
    console.log("create the server tcp socket...")
    server = create_socket()
    console.log(f"socket: {server}")
    server.listen()

    client_id = 100
    try:
        while True:
            client, address = server.accept()
            console.log(f"connected to {address}...")

            thread = threading.Thread(
                target=handle_client, args=(client, address, client_id)
            )
            thread.start()

            client_id += 1

    except ValueError as err:
        print(err)

    finally:
        console.log("closing server down...")
        server.close()


if __name__ == "__main__":
    typer.run(main)
