#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-18 15:08:41

import asyncio
import argparse
import socket

async def client(host, port, message):
    reader, writer = await asyncio.open_connection(host, port)

    # Send the message to the server
    writer.write(message.encode())
    await writer.drain()

    # Receive and print the response from the server
    response = await reader.read(1024)
    print(f"svr-> {response.decode().rstrip()}")

    # Close the connection
    writer.close()
    await writer.wait_closed()

async def main(context):
    host = context.host
    port = context.port
    message = context.message

    for i in range(context.count):
        await client(host, port, message)

    await asyncio.sleep(0.1)

    if context.say_bye:
        await client(host, port, "bye")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            prog="async_client",
            description="client socket service",
            epilog="Version 0.1.0",
        )

    host = socket.gethostbyname(socket.gethostname())

    parser.add_argument('-H', '--host', default=host, help="the target host name or ip addr")
    parser.add_argument('-p', '--port', default=15000, type=int, help="the target port number")
    parser.add_argument('-c', '--count', default=5, type=int, help="how many times to send the message")
    parser.add_argument('-m', '--message', default="rtkey", help="the message to send")
    parser.add_argument('-v', '--verbose', default=False, help="verbose flag")
    parser.add_argument('-s', '--say_bye', default=False, help="close socket with bye message")

    args = parser.parse_args()

    asyncio.run(main(args))
