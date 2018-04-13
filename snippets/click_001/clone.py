import os
import subprocess
import platform

import click
from .os_check import OS_TYPE, OS_Type
from .test001 import cli

@cli.command()
@click.argument('src')
@click.argument('dest', required=False)
@click.pass_obj
def clone(repo, src, dest):
    '''  how to use clone method. 
        here -->
    '''
    click.echo(str(repo))


@cli.command()
def osname():
    os_name = platform.system()
    
    print(os_name)

@cli.command()
def clear():
    if OS_TYPE == OS_Type.WINDOWS:
        os.system('cls')
    else:
        os.system('clear')

@cli.command()
def ls():
    if OS_TYPE == OS_Type.WINDOWS:
        os.system('dir')
    else:
        os.system('ls')
        
@cli.command()
def ll():
    os.system('ls -al')
     

@cli.command()
@click.option('--name', prompt='your name please')
def hello(name):
    click.echo('welcome %s' % name)   

@cli.command()
@click.option('--password', prompt=True, hide_input=True,confirmation_prompt=True)
def encrypy(password):
    click.echo('Encryting password to %s' % password.encode('utf-16'))


def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()

@cli.command()
@click.option('--yes', is_flag=True, callback=abort_if_false, expose_value=False, prompt='Are you sure you want to drop the db?')
def dropdb():
    click.echo('Dropped all tables!!')

@cli.command()
@click.option('--cmd', prompt=' * bash > ')
def call(cmd):
    if cmd:
        result = subprocess.check_output(cmd,shell=True)
        print("{}".format(result.decode('utf-8')))
