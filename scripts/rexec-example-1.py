import rexec

r = rexec.RExec()
print r.r_eval("1+2+3")
print r.r_eval("__import__('os').remove('file')")

## 6
## Traceback (innermost last):
##   File "rexec-example-1.py", line 5, in ?
##     print r.r_eval("__import__('os').remove('file')")
##   File "/usr/local/lib/python1.5/rexec.py", line 257, in r_eval
##     return eval(code, m.__dict__)
##   File "<string>", line 0, in ?
## AttributeError: remove
