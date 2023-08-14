#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-13 15:22:24

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from pydantic import validate_call
from pydantic.types import conint

class User(BaseModel):
    id: str
    name: str = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

@validate_call
def echo_hello(n_times: conint(gt=0, lt=11), name: str, loud: bool):
    greeting = f'Hello {name}!'
    if loud:
        greeting = greeting.upper()

    for i in range(n_times):
        print(greeting)


if __name__ == '__main__':
    print('@see https://medium.com/data-engineer-things/dont-write-another-line-of-code-until-you-see-these-pydantic-v2-breakthrough-features-5cdc65e6b448\n')

    external_data = {'id': '123abc456', 'signup_ts': '2017-06-01 12:22', 'friends': [1, '2', b'3']}
    user = User(**external_data)
    print(user)

    echo_hello(n_times=2, name='dpw', loud=False)
    echo_hello(n_times=2, name='dpw', loud=True)

