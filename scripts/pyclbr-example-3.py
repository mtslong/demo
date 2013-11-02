import pyclbr

# available in Python 2.0 and later
mod = pyclbr.readmodule_ex("cgi")

for k, v in mod.items():
    print k, v

## MiniFieldStorage <pyclbr.Class instance at 00905D2C>
## parse_header <pyclbr.Function instance at 00905BD4>
## test <pyclbr.Function instance at 00906FBC>
## print_environ_usage <pyclbr.Function instance at 00907C94>
## parse_multipart <pyclbr.Function instance at 00905294>
## FormContentDict <pyclbr.Class instance at 008D3494>
## initlog <pyclbr.Function instance at 00904AAC>
## parse <pyclbr.Function instance at 00904EFC>
## StringIO <pyclbr.Class instance at 00903EAC>
## SvFormContentDict <pyclbr.Class instance at 00906824>
## ...
