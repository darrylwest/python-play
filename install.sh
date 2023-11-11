#!/usr/bin/env bash
# dpw@piedmont
# 2023-10-11 12:58:17
#

set -eu

# deps='aiohttp "httpx[http2]" rich mpire faker "redis[hiredis]" textual screeninfo  pywebview pyinvoke black pytest isort'
deps='httpx[http2] rich mpire faker textual screeninfo  pywebview pyinvoke black pytest isort'

for dep in $deps
do
    echo $dep
    python -m pip install $dep
done

exit $?

