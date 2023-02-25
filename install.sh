#!/usr/bin/env bash
# dpw@BCT-MBP.localdomain
# 2023-02-15 15:13:31
#


set -eu

#
# cocalc key sk_2vaIqnuOdJfAVLhd
python3 -m pip install --upgrade pip

# ptpython

packages="numpy sympy scipy matplotlib pandas bokeh dask pymc3 statsmodels sklearn gmpy2 redis"

for p in $packages
do
    python3 -m pip install $p
done

exit $?

