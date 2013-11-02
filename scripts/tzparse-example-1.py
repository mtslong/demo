import os
if not os.environ.has_key("TZ"):
    # set it to something...
    os.environ["TZ"] = "EST+5EDT;100/2,300/2"

# importing this module will parse the TZ variable
import tzparse

print "tzparams", "=>", tzparse.tzparams
print "timezone", "=>", tzparse.timezone
print "altzone", "=>", tzparse.altzone
print "daylight", "=>", tzparse.daylight
print "tzname", "=>", tzparse.tzname

## tzparams => ('EST', 5, 'EDT', 100, 2, 300, 2)
## timezone => 18000
## altzone => 14400
## daylight => 1
## tzname => ('EST', 'EDT')
