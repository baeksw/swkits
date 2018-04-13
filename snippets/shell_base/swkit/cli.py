# coding: utf-8
from __future__ import unicode_literals

import json
import os
import re
import sys

from prompt_toolkit import prompt, AbortAction
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.history import FileHistory
from prompt_toolkit.layout.lexers import PygmentsLexer
from prompt_toolkit.styles.from_pygments import style_from_pygments
from pygments.styles import get_style_by_name
from pygments.util import ClassNotFound

import click
import math
import time
import random
from click_repl import repl
from click_shell import shell
from prompt_toolkit.history import FileHistory


from .xdr import get_data_dir

try:
    range_type = xrange
except NameError:
    range_type = range

from . import __version__, __author__


click.disable_unicode_literals_warning = True


def normalize_url(ctx, param, value):
    if value:
        # business logic
        print('@-- normalize_url ', value)
        return value
    return None


cfg = {
    'pager' : '',
#   'output_stype' : '',
}


DEFAULT_HISTORY = FileHistory(os.path.join(get_data_dir(), 'history'))
DEFAULT_LEXER = None
DEFAULT_COMPLETER = None

@click.command(context_settings=dict(ignore_unknown_options=True,))
@click.option('--spec', help="OpenAPI/Swagger specification file.",callback=normalize_url)
@click.option('--env', help="Environment file to preload.", type=click.Path(exists=True))
@click.argument('url', default='')
@click.argument('http_options',nargs=-1,type=click.UNPROCESSED)
def cli(spec, env, url, http_option):
    click.echo('programing: %s' % __author__)
    click.echo('Version: %s' % __version__)

    os.environ['PAGER'] = cfg['pager']
    os.environ['LESS'] = '-RXF'

    output_style = cfg.get('output_style')
    if output_style:
        context.options['--style'] = output_style
    

    # for prompt-toolkit
    history = FileHistory(os.pa


    while True:
        try:
            text = prompt('shell> ',









