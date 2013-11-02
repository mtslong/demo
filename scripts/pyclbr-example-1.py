import pyclbr

mod = pyclbr.readmodule("cgi")

for k, v in mod.items():
    print k, v

## MiniFieldStorage <pyclbr.Class instance at 7873b0>
## InterpFormContentDict <pyclbr.Class instance at 79bd00>
## FieldStorage <pyclbr.Class instance at 790e20>
## SvFormContentDict <pyclbr.Class instance at 79b5e0>
## StringIO <pyclbr.Class instance at 77dd90>
## FormContent <pyclbr.Class instance at 79bd60>
## FormContentDict <pyclbr.Class instance at 79a9c0>
