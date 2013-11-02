import fileinput
import sys

for line in fileinput.input("samples/sample.txt"):
    sys.stdout.write("-> ")
    sys.stdout.write(line)

## -> We will perhaps eventually be writing only small
## -> modules which are identified by name as they are
## -> used to build larger ones, so that devices like
## -> indentation, rather than delimiters, might become
## -> feasible for expressing local structure in the
## -> source language.
## ->      -- Donald E. Knuth, December 1974
