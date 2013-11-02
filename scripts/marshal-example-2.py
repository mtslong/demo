import marshal

script = """
print 'hello'
"""

code = compile(script, "<script>", "exec")

data = marshal.dumps(code)

# intermediate format
print type(data), len(data)

print "-"*50
print repr(data)
print "-"*50

exec marshal.loads(data)

## <type 'string'> 81
## --------------------------------------------------
## 'c\000\000\000\000\001\000\000\000s\017\000\000\00
## 0\177\000\000\177\002\000d\000\000GHd\001\000S(\00
## 2\000\000\000s\005\000\000\000helloN(\000\000\000\
## 000(\000\000\000\000s\010\000\000\000<script>s\001
## \000\000\000?\002\000s\000\000\000\000'
## --------------------------------------------------
## hello
