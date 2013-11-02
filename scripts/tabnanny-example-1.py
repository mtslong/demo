import tabnanny

FILE = "samples/badtabs.py"

file = open(FILE)
for line in file.readlines():
    print repr(line)

# let tabnanny look at it
tabnanny.check(FILE)

## 'if 1:\012'
## '    \011print "hello"\012'
## '        print "world"\012'
## samples/badtabs.py 3 '        print "world"\012'
