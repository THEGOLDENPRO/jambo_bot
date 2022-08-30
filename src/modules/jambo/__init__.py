'''
This GoldyBot module was generated with VS Code.
'''

import GoldyBot

AUTHOR = 'Dev Goldy'
AUTHOR_GITHUB = 'https://github.com/THEGOLDENPRO'
OPEN_SOURCE_LINK = 'https://github.com/THEGOLDENPRO/jambo_bot/tree/main/src/modules/jambo'

from . import utils

def load():
    # This function get's executed when the module is loaded so run your extenstion classes in here.
    # Example: YourExtenstion(package_module_name=__name__)

    utils.JamboUtils(package_module=__name__)
