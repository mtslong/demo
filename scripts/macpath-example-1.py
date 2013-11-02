import macpath

file = "my:little:pony"

print "isabs", "=>", macpath.isabs(file)
print "dirname", "=>", macpath.dirname(file)
print "basename", "=>", macpath.basename(file)
print "normpath", "=>", macpath.normpath(file)
print "split", "=>", macpath.split(file)
print "join", "=>", macpath.join(file, "zorba")

## isabs => 1
## dirname => my:little
## basename => pony
## normpath => my:little:pony
## split => ('my:little', 'pony')
## join => my:little:pony:zorba
