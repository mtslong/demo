import ntpath

file = "/my/little/pony"

print "isabs", "=>", ntpath.isabs(file)
print "dirname", "=>", ntpath.dirname(file)
print "basename", "=>", ntpath.basename(file)
print "normpath", "=>", ntpath.normpath(file)
print "split", "=>", ntpath.split(file)
print "join", "=>", ntpath.join(file, "zorba")

## isabs => 1
## dirname => /my/little
## basename => pony
## normpath => \my\little\pony
## split => ('/my/little', 'pony')
## join => /my/little/pony\zorba
