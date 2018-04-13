'''Functions that deal with the user configuration.'''

import os
from swkit import defaultconfig

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_user_config_path():
    '''Get the path to the user config file.'''
    return os.path.join(BASE_DIR, 'config.py')


def initialize():
    '''Initialize a default config file if it doesn't exist yet
    
    Returns:
        tuple: A tuple of (copied, dist_path). `copied` is a bool indicating if this function created the default config file. `dist_path` is the path of the user config file.

    '''
    return get_user_config_path()

def _module_to_dict(module):
    attrs = {}
    attr_names = filter(lambda n: not n.startswith('_'), dir(module))
    for name in attr_names:
        value = getattr(module, name)
        attrs[name] = value
    return attrs


