#!/usr/bin/env bash
# dpw@tiburon.localdomain
# 2023-09-14 19:23:39
#

set -eu

port=9040
echo "running on port $port"
python3 -m http.server $port --bind 127.0.0.1

