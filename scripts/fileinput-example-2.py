import fileinput
import glob
import string, sys

for line in fileinput.input(glob.glob("samples/*.txt")):
    if fileinput.isfirstline(): # first in a file?
        sys.stderr.write("-- reading %s --\n" % fileinput.filename())
    sys.stdout.write(str(fileinput.lineno()) + " " + string.upper(line))

## -- reading samples\sample.txt --
## 1 WE WILL PERHAPS EVENTUALLY BE WRITING ONLY SMALL
## 2 MODULES WHICH ARE IDENTIFIED BY NAME AS THEY ARE
## 3 USED TO BUILD LARGER ONES, SO THAT DEVICES LIKE
## 4 INDENTATION, RATHER THAN DELIMITERS, MIGHT BECOME
## 5 FEASIBLE FOR EXPRESSING LOCAL STRUCTURE IN THE
## 6 SOURCE LANGUAGE.
## 7    -- DONALD E. KNUTH, DECEMBER 1974
