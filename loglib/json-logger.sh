#!/usr/bin/env bash
# dpw@plaza.localdomain
# 2023-08-22 17:20:24
#

set -eu

curl -X 'POST' \
  'http://10.0.1.105:15010/v1/logit/test' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "test",
  "msg": "my test message",
  "levelname": "INFO",
  "filename": "applogger.py",
  "lineno": 10,
  "created": 2330.433,
  "asctime": "2023-08-22 17:16:07.1692753367",
  "other": ["Thread=name", "Morestuff=sss"]
}'
