import pyclbr
import string

mod = pyclbr.readmodule("cgi")

def dump(c):
    # print class header
    s = "class " + c.name
    if c.super:
        s = s +  "(" + string.join(map(lambda v: v.name, c.super), ", ") + ")"
    print s + ":"
    # print method names, sorted by line number
    methods = c.methods.items()
    methods.sort(lambda a, b: cmp(a[1], b[1]))
    for method, lineno in methods:
        print "  def " + method
    print

for k, v in mod.items():
    dump(v)

## class MiniFieldStorage:
##   def __init__
##   def __repr__
##
## class InterpFormContentDict(SvFormContentDict):
##   def __getitem__
##   def values
##   def items
##
## ...
