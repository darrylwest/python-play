#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-17 19:27:23


import asyncio
import uvloop


async def handle_client(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info("peername")

    print(f"Received {message!r} from {addr!r}")

    print("Send: {!r}".format(message))
    writer.write(data)
    await writer.drain()

    print("Closing the connection")
    writer.close()


async def main(port: int = 15000):
    server = await asyncio.start_server(handle_client, "::1", port)

    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
