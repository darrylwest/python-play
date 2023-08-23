#!/usr/bin/env bash
# dpw@plaza.localdomain
# 2023-08-22 17:20:24
#

set -eu

curl -X 'POST' \
  "http://$LOCAL_IP:15010/v1/logit/test" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "test",
  "msg": "my test message",
  "level": "INFO",
  "filename": "applogger.py",
  "lineno": 10,
  "created": 2330.433,
  "asctime": "2023-08-22 17:16:07.1692753367",
  "other": ["Thread=name", "Morestuff=sss"]
}'
