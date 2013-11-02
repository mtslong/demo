import marshal

value = (
    "this is a string",
    [1, 2, 3, 4],
    ("more tuples", 1.0, 2.3, 4.5),
    "this is yet another string"
    )

data = marshal.dumps(value)

# intermediate format
print type(data), len(data)

print "-"*50
print repr(data)
print "-"*50

print marshal.loads(data)

## <type 'string'> 118
## --------------------------------------------------
## '(\004\000\000\000s\020\000\000\000this is a string
## [\004\000\000\000i\001\000\000\000i\002\000\000\000
## i\003\000\000\000i\004\000\000\000(\004\000\000\000
## s\013\000\000\000more tuplesf\0031.0f\0032.3f\0034.
## 5s\032\000\000\000this is yet another string'
## --------------------------------------------------
## ('this is a string', [1, 2, 3, 4], ('more tuples',
## 1.0, 2.3, 4.5), 'this is yet another string')
