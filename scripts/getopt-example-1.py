import getopt
import sys

# simulate command line invocation
sys.argv = ["myscript.py", "-l", "-d", "directory", "filename"]

# process options
opts, args = getopt.getopt(sys.argv[1:], "ld:")

long = 0
directory = None

for o, v in opts:
    if o == "-l":
        long = 1
    elif o == "-d":
        directory = v

print "long", "=", long
print "directory", "=", directory
print "arguments", "=", args

## long = 1
## directory = directory
## arguments = ['filename']
