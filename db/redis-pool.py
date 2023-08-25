#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-25 16:42:26

import sys
import os
from rich import print, inspect
import redis

import redis

def connect():
    # this has to be set in the current env
    redis_auth = os.getenv("REDISCLI_AUTH")
    print(redis_auth)

    redis_port = os.getenv("REDIS_PORT", 6452)
    print(redis_port)

    redis.Redis(decode_responses=True)

    # Create a Redis connection object
    r = redis.Redis(
        host='localhost',
        port=redis_port,
        password=redis_auth,
        # ssl=True,
        # ssl_cert_reqs=None,
        client_name='my-service',
        health_check_interval=30,
    )

    # Set the Redis protocol version to RESP3
    r.connection_pool.connection_kwargs['client_name'] = 'my-service'
    r.connection_pool.connection_kwargs['health_check_interval'] = 30

    print("connecting")
    r.connection_pool.get_connection('PING', None).send_command('HELLO', 3)

    return r

def write_pipeline(db):
    values = {str(x*3) : f'v-{x*x}' for x in range(1,10)}

    pipe = db.pipeline()
    for k,v in values.items():
        print(f'{k}={v}')
        resp = pipe.set(k, v)

    resp = pipe.execute()
    print(f'pipe response: {resp}')
    assert all(resp)

def scan_test(db):
    for key in db.scan_iter('*', 100, _type='STRING'):
        print(key)

def main(args: list) -> None:
    db = connect()

    print(db)

    # conn = db.connection_pool.get_connection('PING', None)
    # inspect(conn)

    size = db.dbsize()
    print(f'size: {size}')

    value = db.get('mykey')
    print(f'value {value}')


    resp = db.set('my_new_key', 'my new shiny value')
    print(f'resp: {resp}')

    value = db.get('my_new_key')
    print(f'value {value}')

    write_pipeline(db)

    scan_test(db)

    resp = db.save()
    print(f'save: {resp}')


if __name__ == '__main__':
    # read the .env file?
    main(sys.argv[1:])

