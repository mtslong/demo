import os
import time

file = "samples/sample.jpg"

def dump(st):
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
    print "- size:", size, "bytes"
    print "- owner:", uid, gid
    print "- created:", time.ctime(ctime)
    print "- last accessed:", time.ctime(atime)
    print "- last modified:", time.ctime(mtime)
    print "- mode:", oct(mode)
    print "- inode/dev:", ino, dev

#
# get stats for a filename

st = os.stat(file)

print "stat", file
dump(st)
print

#
# get stats for an open file

fp = open(file)

st = os.fstat(fp.fileno())

print "fstat", file
dump(st)

## stat samples/sample.jpg
## - size: 4762 bytes
## - owner: 0 0
## - created: Tue Sep 07 22:45:58 1999
## - last accessed: Sun Sep 19 00:00:00 1999
## - last modified: Sun May 19 01:42:16 1996
## - mode: 0100666
## - inode/dev: 0 2
##
## fstat samples/sample.jpg
## - size: 4762 bytes
## - owner: 0 0
## - created: Tue Sep 07 22:45:58 1999
## - last accessed: Sun Sep 19 00:00:00 1999
## - last modified: Sun May 19 01:42:16 1996
## - mode: 0100666
## - inode/dev: 0 0
