'''Usage:
    my_program tcp <host> <port> [--timeout=<second>]
    my_program serial <port> [--baud=9600] [--timeout=<second>]
    my_program (-h | --help | --version)
'''
import sys
from docopt import docopt

print(docopt(__doc__, version='1.0.0rc2'))
