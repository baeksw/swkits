'''Usage: pep8 [options] <input>...

Options:
    --version           show program's version number and exit
    -h, --help          show this help message and exit
    -v, --verbose       print status message, or debug with -vv
    -q, --quiet         report only file names, or nothing with -qq
    --exclude=patterns  exclude files or directories which match these comma
                        separated patterns [default: .svn,CVS,.bzr,.hg,.git]
    --filename=patterns when parsing directories, only check filenames matching
    --select=errors     select errors and warnings (e.g. E,W6)
    --ignore=errors     skip errors and warnings
'''
import sys
from docopt import docopt

print(docopt(__doc__, version='1.0.0rc2'))
