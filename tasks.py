'''
task runner, @see https://docs.pyinvoke.org/en/stable/index.html
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
