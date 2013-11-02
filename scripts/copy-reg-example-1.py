import pickle

CODE = """
print 'good evening'
"""

code = compile(CODE, "<string>", "exec")

exec code
exec pickle.loads(pickle.dumps(code))

## good evening
## Traceback (innermost last):
## ...
## pickle.PicklingError: can't pickle 'code' objects
