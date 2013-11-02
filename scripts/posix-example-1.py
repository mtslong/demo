import posix

for file in posix.listdir("."):
    print file, posix.stat(file)[6]

## aifc-example-1.py 314
## anydbm-example-1.py 259
## array-example-1.py 48
