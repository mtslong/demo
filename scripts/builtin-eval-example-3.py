print eval("__import__('os').getcwd()", {})
print eval("__import__('os').remove('file')", {"__builtins__": {}})

## /home/fredrik/librarybook
## Traceback (innermost last):
##   File "builtin-eval-example-3.py", line 2, in ?
##   File "<string>", line 0, in ?
## NameError: __import__
