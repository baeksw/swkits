import os
import click
from click_shell import shell

INTRO = '''

SW-KITS
  - mssql utils

'''

@shell(prompt='sw-mssql > ', intro = INTRO)
@click.option('--config', default='config.json')
@click.pass_context
def cli(ctx, config):
    pass
