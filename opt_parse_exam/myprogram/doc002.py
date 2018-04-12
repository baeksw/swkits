'''Usage:
    my_program command --option <argument>
    my_program [<optional-argument>]
    my_program --another-option=<with-argument>
    my_program (--either-that-option | <or-this-argument>)
    my_program <repeating-argument> <repeating-argument>...
'''
import sys
from docopt import docopt

print(docopt(__doc__, version='1.0.0rc2'))
