#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-10-13 22:35:01

# NOTE: pub/sub is good for fire and forget, but streams are much better for database replication ops

import asyncio
import redis.asyncio as redis

from rich import print

STOPWORD = "STOP"

class UserPubSub:
    def __init__(self, client: redis.Redis):
        self.client = client


    async def listener(self, channel: redis.client.PubSub):
        while True:
            message = await channel.get_message(ignore_subscribe_messages=True)
            if message is not None:
                print(f"(update) Message Received: {message}")
                if message["data"].decode() == STOPWORD:
                    print("(Reader) STOP")
                    break

                match message.get('channel'):
                    case b'user:update':
                        key = message.get('data')
                        jstr = await self.client.get(key)
                        print(f'update: {jstr}')
                    case b'user:remove':
                        key = message.get('data')
                        print(f'remove: {key}')
                    case other:
                        print(f'ERROR: {other}')



    async def start(self) -> None:
        r = self.client
        pong = await r.ping()
        assert pong, 'database ping failed'

        async with r.pubsub() as pubsub:
            await pubsub.subscribe("user:update","user:remove")

            future = asyncio.create_task(self.listener(pubsub))

            await r.publish("user:update", "US477ls2Ci9Jiqrn")
            await r.publish("user:update", "USe37ls2DWZozWhr")

            await future

        await r.aclose()

if __name__ == '__main__':
    print('''[green3]Do this from redis cli...

    [cyan]redis-cli -a testpw

    publish user:update USa37ls20XhfJCFr
    publish user:remove some-key


    # then stop the service...
    publish user:update STOP
    ''')

    redis_auth = 'testpw'
    redis_port = 6379

    r = redis.Redis(
        host='localhost',
        port=redis_port,
        db=1,
        password=redis_auth,
        protocol=3,
    )

    pubsub = UserPubSub(r)

    asyncio.run(pubsub.start())

