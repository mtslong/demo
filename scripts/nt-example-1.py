import nt

# in real life, use os.listdir and os.stat instead!
for file in nt.listdir("."):
    print file, nt.stat(file)[6]

## aifc-example-1.py 314
## anydbm-example-1.py 259
## array-example-1.py 48
