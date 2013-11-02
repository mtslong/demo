import string

text = "Monty Python's Flying Circus"

print "upper", "=>", string.upper(text)
print "lower", "=>", string.lower(text)
print "split", "=>", string.split(text)
print "join", "=>", string.join(string.split(text), "+")
print "replace", "=>", string.replace(text, "Python", "Java")
print "find", "=>", string.find(text, "Python"), string.find(text, "Java")
print "count", "=>", string.count(text, "n")

## upper => MONTY PYTHON'S FLYING CIRCUS
## lower => monty python's flying circus
## split => ['Monty', "Python's", 'Flying', 'Circus']
## join => Monty+Python's+Flying+Circus
## replace => Monty Java's Flying Circus
## find => 6 -1
## count => 3
