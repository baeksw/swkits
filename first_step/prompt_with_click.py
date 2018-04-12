from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter
import click

DEFAULT_HISTORY = FileHistory('history.txt')
DEFAULT_SUGGEST = AutoSuggestFromHistory()

SQL_COMPLETER = WordCompleter(
                        ['select', 'from', 'insert', 'update', 'delete', 'drop'],
                        ignore_case=True)

while True:
    user_input = prompt('sw_kit> '
                , history=DEFAULT_HISTORY
                , auto_suggest = DEFAULT_SUGGEST
                , completer = SQL_COMPLETER
                )
    click.echo_via_pager(user_input)
