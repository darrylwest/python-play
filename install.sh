#!/usr/bin/env bash
# dpw@piedmont
# 2023-10-11 12:58:17
#

set -eu

[ `uname` != "Linux" ] && {
    echo "should only run this script on Linux machines..."
    exit -1
}

deps='bpython aiohttp "httpx[http2]" rich mpire faker "redis[hiredis]" textual screeninfo  pywebview pyinvoke black pytest isort'

for dep in $deps
do
    echo $dep
    python -m pip install $dep
done

exit $?

