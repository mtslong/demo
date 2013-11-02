import imp
import sys

def my_import(name, globals=None, locals=None, fromlist=None):
    try:
        module = sys.modules[name] # already imported?
    except KeyError:
        file, pathname, description = imp.find_module(name)
        print "import", name, "from", pathname, description
        module = imp.load_module(name, file, pathname, description)
    return module

import __builtin__
__builtin__.__import__ = my_import

import xmllib

## import xmllib from /python/lib/xmllib.py ('.py', 'r', 1)
## import re from /python/lib/re.py ('.py', 'r', 1)
## import sre from /python/lib/sre.py ('.py', 'r', 1)
## import sre_compile from /python/lib/sre_compile.py ('.py', 'r', 1)
## import _sre from /python/_sre.pyd ('.pyd', 'rb', 3)
