#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-02-06 19:01:37
#

import requests as rq

url = "https://raincitysoftware.com"
r = rq.get(url)

print(r.text)
print(f"response status: {r.status_code}")
