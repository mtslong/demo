print eval("__import__('os').getcwd()")
print eval("__import__('os').remove('file')")

## /home/fredrik/librarybook
## Traceback (innermost last):
##  File "builtin-eval-example-2", line 2, in ?
##  File "<string>", line 0, in ?
## os.error: (2, 'No such file or directory')
