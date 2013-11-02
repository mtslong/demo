import pdb

def test(n):
    j = 0
    for i in range(n):
        j = j + i
    return n

db = pdb.Pdb()
db.runcall(test, 1)

## > pdb-example-1.py(3)test()
## -> def test(n):
## (Pdb) s
## > pdb-example-1.py(4)test()
## -> j = 0
## (Pdb) s
## > pdb-example-1.py(5)test()
## -> for i in range(n):
## ...
