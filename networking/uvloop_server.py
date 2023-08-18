#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-17 19:27:23


import os
import asyncio
import signal
import uvloop


async def shutdown(loop, server):
    server.close()
    await server.wait_closed()

    tasks = [t for t in asyncio.all_tasks(loop) if t is not asyncio.current_task(loop)]

    for task in tasks:
        task.cancel()

    await asyncio.gather(*tasks, return_exceptions=True)

    loop.stop()


async def handle_client(reader, writer):
    try:
        addr = writer.get_extra_info("peername")
        while True:
            data = await reader.read(1024)
            if not data:
                break

            message = data.decode().rstrip()

            response = "ok".encode()
            print(f"client-> {message} from {addr!r}, response: {response}")

            writer.write(response)
            await writer.drain()

    except ValueError as err:
        print(err)

    except Exception as ex:
        print(f"An exception was detected: {ex}")

    finally:
        print("closing the connection")
        writer.close()


async def main(port: int = 15000):
    try:
        loop = uvloop.new_event_loop()
        asyncio.set_event_loop(loop)

        server = await asyncio.start_server(handle_client, "::1", port)

        addr = server.sockets[0].getsockname()
        print(f"Serving on {addr}")

        await server.serve_forever()

    except asyncio.CancelledError:
        pass

    finally:
        await shutdown(loop, server)
        print("out...")


if __name__ == "__main__":
    pid = os.getpid()
    print(f"{pid=}")

    with open("uvloop-server.pid", "w") as f:
        f.write(str(pid))

    uvloop.install()
    asyncio.run(main())
