import nis
import string

print nis.cat("ypservers")
print string.split(nis.match("bacon", "hosts.byname"))

## {'bacon.spam.egg': 'bacon.spam.egg'}
## ['194.18.155.250', 'bacon.spam.egg', 'bacon', 'spam-010']
