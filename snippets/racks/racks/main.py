#-*- coding: utf-8 -*-
"""
Usage: racks <numbers>...

Example 
    racks 1 25 221 57 32 68 9

Option 
    -h, --help      show this screen
    -v, --version   show version
"""

from docopt import docopt
from racks import __version__
from termcolor import cprint

steps = 'ABCDEFG'

def normalize_numbers(numbers):
    '''
    Given a list of numbers normalize the given numbers to 0 - 6
    to allow each number to account for the number of different unicode block
    we have to represent them.
    '''
    step_range = max(numbers) - min(numbers)
    step = ((step_range) / float(6)) or 1
    rack = ' '.join(steps[int(round((n - min(numbers)) / step))] for n in numbers)
    cprint(rack, 'green')


def start():
    version = ".".join("{0}".format(x) for x in __version__)
    arguments = docopt(__doc__, version=version)
    numbers = arguments.get('<numbers>', None)
    if numbers:
        try:
            numbers = map(int, numbers)
            normalize_numbers(numbers)
        except ValueError:
            cprint("Racks only accepts integers " , "red")



