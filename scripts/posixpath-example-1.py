import posixpath

file = "/my/little/pony"

print "isabs", "=>", posixpath.isabs(file)
print "dirname", "=>", posixpath.dirname(file)
print "basename", "=>", posixpath.basename(file)
print "normpath", "=>", posixpath.normpath(file)
print "split", "=>", posixpath.split(file)
print "join", "=>", posixpath.join(file, "zorba")

## isabs => 1
## dirname => /my/little
## basename => pony
## normpath => /my/little/pony
## split => ('/my/little', 'pony')
## join => /my/little/pony/zorba
