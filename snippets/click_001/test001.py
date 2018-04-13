import os
import click
from click_shell import shell

class Repo(object):
    def __init__(self, home=None, debug=False):
        self.home = home
        self.debug = debug
    def __str__(self):
        return "{} - {}".format(self.home, self.debug)

@shell(prompt='myapp> ', intro='''HE''')
#@click.group()
@click.option('--repo-home', envvar='REPO_HOME', default='.repo')
@click.option('--debug/--no-debug', default=False, envvar='REPO_DEBUG')
@click.pass_context
def cli(ctx, repo_home, debug):
    ctx.obj = Repo(repo_home, debug)

