#!/usr/bin/env bash
# dpw@BCT-MBP.localdomain
# 2023-02-15 15:13:31
#

set -eu

#
#
# python -m pip install --upgrade pip

# repl: ptpython
# pip3 install --upgrade jupyterlab-vim

# python3 -m pip install --upgrade "redis[hiredis]"

# packages='numpy sympy scipy seaborn pandas bokeh dask pymc3 sklearn gmpy2'
packages='clicky schedule requests httpx pyvibe black isort matplotlib plotly statsmodels'

for p in $packages
do
    echo "$p ##### ##### ##### ##### ##### ##### ##### ##### ##### #####"
    python -m pip install --upgrade $p
done

exit $?

