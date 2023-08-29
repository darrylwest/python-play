#!/usr/bin/env python3
# dpw@tiburon.localdomain
# 2023-08-29 21:43:05

import asyncio

async def background_task():
    print("Do some long-running task here.", flush=True)
    await asyncio.sleep(5)
    print('Background task finished.')

async def main():
    print("Create a task for the background task.", flush=True)
    task = asyncio.create_task(background_task())

    # Do other work here.

    print('Wait for the background task to finish.', flush=True)
    await task

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
