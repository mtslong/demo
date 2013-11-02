import copy_reg
import pickle, types
import StringIO

#
# register a pickle handler for file objects

def file_unpickler(position, data):
    file = StringIO.StringIO(data)
    file.seek(position)
    return file

def file_pickler(code):
    position = file.tell()
    file.seek(0)
    data = file.read()
    file.seek(position)
    return file_unpickler, (position, data)

copy_reg.pickle(types.FileType, file_pickler, file_unpickler)

#
# try it out

file = open("samples/sample.txt", "rb")

print file.read(120),
print "<here>",
print pickle.loads(pickle.dumps(file)).read()

## We will perhaps eventually be writing only small
## modules which are identified by name as they are
## used to build larger <here>  ones, so that devices like
## indentation, rather than delimiters, might become
## feasible for expressing local structure in the
## source language.
##      -- Donald E. Knuth, December 1974
