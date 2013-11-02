import packmail
import sys

packmail.pack(sys.stdout, "samples/sample.txt", "sample.txt")

## echo sample.txt
## sed "s/^X//" >sample.txt <<"!"
## XWe will perhaps eventually be writing only small
## Xmodules which are identified by name as they are
## Xused to build larger ones, so that devices like
## Xindentation, rather than delimiters, might become
## Xfeasible for expressing local structure in the
## Xsource language.
## X    -- Donald E. Knuth, December 1974
## !
