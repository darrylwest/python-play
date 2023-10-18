'''
task runner, @see https://www.pyinvoke.org/
'''

from invoke import task
from sysconfig import get_paths

@task
def build(ctx):
    info = get_paths()
    include = info['include']

    cmd = f'gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -lm -I{include} -o hello.so hello.c'
    ctx.run(cmd)

@task
def clean(ctx):
    ctx.run('rm -f *.c *.so')
