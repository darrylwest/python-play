"""
task runner, @see https://www.pyinvoke.org/
"""

from sysconfig import get_paths

from invoke import task


@task
def build(ctx):
    info = get_paths()
    include = info["include"]

    ctx.run("cython hello.pyx")

    cmd = f"gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -lm -I{include} -o hello.so hello.c"
    ctx.run(cmd)


@task
def clean(ctx):
    ctx.run("rm -f *.c *.so")
