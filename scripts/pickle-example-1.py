import pickle

value = (
    "this is a string",
    [1, 2, 3, 4],
    ("more tuples", 1.0, 2.3, 4.5),
    "this is yet another string"
    )

data = pickle.dumps(value)

# intermediate format
print type(data), len(data)

print "-"*50
print data
print "-"*50

print pickle.loads(data)

## <type 'string'> 121
## --------------------------------------------------
## (S'this is a string'
## p0
## (lp1
## I1
## aI2
## aI3
## aI4
## a(S'more tuples'
## p2
## F1.0
## F2.3
## F4.5
## tp3
## S'this is yet another string'
## p4
## tp5
## .
## --------------------------------------------------
## ('this is a string', [1, 2, 3, 4], ('more tuples',
## 1.0, 2.3, 4.5), 'this is yet another string')
