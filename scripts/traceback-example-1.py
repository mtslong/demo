# note! importing the traceback module messes up the
# exception state, so you better do that here and not
# in the exception handler
import traceback

try:
    raise SyntaxError, "example"
except:
    traceback.print_exc()

## Traceback (innermost last):
##   File "traceback-example-1.py", line 7, in ?
## SyntaxError: example
