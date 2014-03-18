"""
A resurrection of some old functions from Python 2. These should be used
sparingly, to help with porting efforts, since code using them is no
longer standard Python 3 code.

We provide these builtin functions which have no equivalent on Py3:

- cmp()
- execfile()

These aliases are also provided:

- raw_input() <- input()
- unicode() <- str()
- unichr() <- chr()

For reference, the following Py2 builtin functions are available from
these standard locations on both Py2.6+ and Py3:

- reduce() <- functools.reduce()
- reload() <- imp.reload()

"""

from past.builtins.noniterators import (filter, map, range, reduce, zip)
from past.builtins.types import basestring, dict, str, long, unicode
# from past.builtins.misc import (ascii, chr, hex, input, oct, open, raw_input, unichr)
from past.builtins.misc import (apply, cmp, execfile, intern, raw_input,
                                reload, unichr, unicode, xrange)
from past import utils


if utils.PY3:
    # We only import names that shadow the builtins on Py3. No other namespace
    # pollution on Py3.
    
    # Only shadow builtins on Py3; no new names
    __all__ = ['filter', 'map', 'range', 'zip', 
               'basestring', 'dict', 'str',
               'cmp', 'execfile', 'raw_input', 'reduce', 'reload',
               'unichr', 'unicode', 'xrange'
    #            'ascii', 'chr', 'hex', 'input', 'oct', 'open', 'unichr',
    #            'bytes', 'dict', 'int', 'range', 'round', 'str', 'super',
              ]

else:
    # No namespace pollution on Py2
    __all__ = []
