import os
import click

from .load_group import cli

@cli.command()
def clear():
    click.clear()








@cli.command()
def edit():
    click.edit('/tmp/tmp.txt')













def start():
    cli()
