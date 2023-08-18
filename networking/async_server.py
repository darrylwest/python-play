#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-16 23:17:11

import asyncio
import socket


async def handle_client(reader, writer):
    print(f"handle client: {reader}", flush=True)

    request = None
    while request != "shutdown":
        request = (await reader.read(1024)).decode("utf8")

        print(f"client<-{request}", flush=True)

        response = "ok\n"

        writer.write(response.encode("utf8"))

        await writer.drain()

    writer.close()
    print(f"closing {reader}", flush=True)


async def server(port: int = 16000):
    host = socket.gethostbyname(socket.gethostname())
    server = await asyncio.start_server(handle_client, host, port)
    print(f"listening on {host}:{port}", flush=True)

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(server())
