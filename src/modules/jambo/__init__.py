'''
This GoldyBot module was generated with VS Code.
'''

import GoldyBot

AUTHOR = 'Dev Goldy'
AUTHOR_GITHUB = 'https://github.com/THEGOLDENPRO'
OPEN_SOURCE_LINK = ''

from . import utils

def load():
    # This function get's executed when the module is loaded so run your extenstion classes in here.
    # Example: YourExtenstion(package_module_name=__name__)

    utils.JamboUtils(package_module=__name__)