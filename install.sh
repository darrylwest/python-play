#!/usr/bin/env bash
# dpw@BCT-MBP.localdomain
# 2023-02-15 15:13:31
#

set -eu

python3 -m pip install --upgrade pip

packages="numpy sympy scipy matplotlib pandas bokeh dask pymc3"

for p in $packages
do
    python3 -m pip install $p
done

exit $?

