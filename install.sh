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

packages="numpy sympy scipy matplotlib seaborn plotly pandas begins bokeh dask pymc3 statsmodels sklearn gmpy2 redis schedule requests httpx pyvibe"

for p in $packages
do
    python3 -m pip install $p
done

exit $?

