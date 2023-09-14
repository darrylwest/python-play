#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-03-10 21:45:37
#

# @see https://schedule.readthedocs.io/

import threading
import time

import schedule


# no input args; with args, use functools.partial to define
def job():
    print(
        f"working at {time.time()} on thread {threading.current_thread()}", flush=True
    )


def run_threaded(func):
    jthread = threading.Thread(target=func)
    jthread.start()


schedule.every(5).seconds.do(run_threaded, job)  # or job, *args, **kwargs)

n = 60
while n > 0:
    schedule.run_pending()
    time.sleep(1)
    n -= 1
