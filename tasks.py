'''
task runner, @see https://www.pyinvoke.org/
'''

from invoke import task
from rich import inspect

@task
def build(ctx):
    '''
    build it
    '''
    print("building...")
    inspect(ctx)

@task
def format(ctx):
    '''
    run black on all python files
    '''
    ctx.run('black */*.py')
    ctx.run('isort */*.py')

@task
def archive(ctx):
    ctx.run('tar czvf data.tgz data/xyz.*')

