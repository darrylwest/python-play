#!/usr/bin/env bash
# dpw@BCT-MBP.localdomain
# 2023-02-15 15:13:31
#

set -eu

#
#
python3 -m pip install --upgrade pip

# repl: ptpython
# pip3 install --upgrade jupyterlab-vim

# packages="numpy sympy scipy seaborn pandas bokeh dask pymc3 sklearn gmpy2"
# packages="matplotlib plotly statsmodels "redis[hiredis]" 
packages="schedule requests httpx pyvibe black isort"

for p in $packages
do
    python3 -m pip install --upgrade $p
done

exit $?

