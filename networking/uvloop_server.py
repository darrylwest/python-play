#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-17 19:27:23


import asyncio
import signal
import uvloop


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
        print(f'An exception was detected: {ex}')

    finally:
        print("closing the connection")
        writer.close()

async def main(port: int = 15000):
    try:
        server = await asyncio.start_server(handle_client, "::1", port)

        addr = server.sockets[0].getsockname()
        print(f"Serving on {addr}")

        async with server:
            await server.serve_forever()

    except Exception as ex:
        print(f'exception: {ex}')

    finally:
        print('out...')

if __name__ == "__main__":
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)

    def shutdown():
        loop.stop()

    loop.add_signal_handler(signal.SIGINT, shutdown)
    loop.add_signal_handler(signal.SIGTERM, shutdown)

    try:
        print(f'run the loop with shutdown handler...')
        loop.run_until_complete(main())
    finally:
        print(f'close the loop');
        loop.close()

