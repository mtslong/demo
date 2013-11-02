def dump(value):
    print value, "=>", dir(value)

import sys

dump(0)
dump(1.0)
dump(0.0j) # complex number
dump([]) # list
dump({}) # dictionary
dump("string")
dump(len) # function
dump(sys) # module

## 0 => []
## 1.0 => []
## 0j => ['conjugate', 'imag', 'real']
## [] => ['append', 'count', 'extend', 'index', 'insert',
##     'pop', 'remove', 'reverse', 'sort']
## {} => ['clear', 'copy', 'get', 'has_key', 'items',
##     'keys', 'update', 'values']
## string => []
## <built-in function len> => ['__doc__', '__name__', '__self__']
## <module 'sys' (built-in)> => ['__doc__', '__name__',
##     '__stderr__', '__stdin__', '__stdout__', 'argv',
##     'builtin_module_names', 'copyright', 'dllhandle',
##     'exc_info', 'exc_type', 'exec_prefix', 'executable',
## ...
