#!/usr/bin/env python3.11
# dpw@plaza.localdomain
# 2023-11-28 16:06:12

import sys
from rich import inspect
import pywhatkit as kit

def main(args: list) -> None:
    print(f'{args}')
    phone = "+17752508168"
    message = "2. hellow from plaza dr"

    resp = kit.sendwhatmsg_instantly(phone, message)

    inspect(resp)

if __name__ == '__main__':
    main(sys.argv[1:])

