import time

now = time.time()

print now, "seconds since", time.gmtime(0)[:6]
print
print "or in other words:"
print "- local time:", time.localtime(now)
print "- utc:", time.gmtime(now)

## 937758359.77 seconds since (1970, 1, 1, 0, 0, 0)
##
## or in other words:
## - local time: (1999, 9, 19, 18, 25, 59, 6, 262, 1)
## - utc: (1999, 9, 19, 16, 25, 59, 6, 262, 0)
