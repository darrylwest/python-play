#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-17 19:27:23


import os
import asyncio
import signal
import uvloop
import subprocess
import socket
import argparse
from collections import namedtuple


async def shutdown(loop, server):
    server.close()
    await server.wait_closed()

    tasks = [t for t in asyncio.all_tasks(loop) if t is not asyncio.current_task(loop)]

    for task in tasks:
        task.cancel()

    await asyncio.gather(*tasks, return_exceptions=True)

    loop.stop()


def create_key() -> str:
    """return a 16 character routing key"""
    result = subprocess.run("rtkey", capture_output=True, text=True)
    key = result.stdout
    return key[0:16]

async def handle_client(reader, writer):
    try:
        addr = writer.get_extra_info("peername")
        while True:
            data = await reader.read(1024)
            if not data:
                break

            message = data.decode("utf-8").rstrip()

            cmd = message[0:3].lower()

            response = "ok\r\n".encode("utf-8")
            match cmd:
                case "bye":
                    print('goodbye...')
                    break
                case "rtk":
                    key = create_key()
                    response = f"{key}\r\n".encode("utf-8")
                case "pin":
                    response = "pong\r\n".encode("utf-8")
                case "ver":
                    response = "0.1.0\r\n".encode("utf-8")
                case _:
                    response = "what?\r\n".encode("utf-8")

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


async def main(context):
    # the host machine's ip address; the service is open to the local network without a proxy
    host = context.host
    port = context.port

    print(f'starting the service, Version: {ctx.version}')

    try:
        loop = uvloop.new_event_loop()
        asyncio.set_event_loop(loop)

        server = await asyncio.start_server(handle_client, host, port)

        addr = server.sockets[0].getsockname()
        print(f"Serving on {addr}")

        await server.serve_forever()

    except asyncio.CancelledError:
        pass

    finally:
        await shutdown(loop, server)
        print("out...")

def create_context():
    """Create the default context and return as a named tuple"""

    Context = namedtuple("Context", "host port verbose version")
    return Context(
            socket.gethostbyname(socket.gethostname()), 
            15000, 
            False,
            "0.1.0",
        )

def write_pid_file():
    pid = os.getpid()
    with open("uvloop-server.pid", "w") as f:
        f.write(str(pid))

    print(f"{pid=}")

if __name__ == "__main__":
    ctx = create_context()

    parser = argparse.ArgumentParser(
            prog="uvloop_server",
            description="uvloop socket server",
            epilog=f"Version {ctx.version}",
        )


    parser.add_argument('-H', '--host', default=ctx.host, help="the server host name or ip addr")
    parser.add_argument('-p', '--port', default=ctx.port, type=int, help="the server port number to listen on")

    args = parser.parse_args()

    write_pid_file()

    uvloop.install()
    asyncio.run(main(args))
