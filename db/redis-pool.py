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

    resp = r.connection_pool.get_connection('PING', None).send_command('KEYS', '*')
    print(f'keys the hard way: {resp}')

    return r


def main(args: list) -> None:
    db = connect()

    print(db)

    # conn = db.connection_pool.get_connection('PING', None)
    # inspect(conn)

    keys = db.keys(pattern='*')
    print(f'keys: {keys}')

    value = db.get('mykey')
    print(f'value {value}')


    resp = db.set('my_new_key', 'my new shiny value')
    print(f'resp: {resp}')

    value = db.get('my_new_key')
    print(f'value {value}')


if __name__ == '__main__':
    # read the .env file?
    main(sys.argv[1:])

