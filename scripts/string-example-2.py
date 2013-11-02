text = "Monty Python's Flying Circus"

print "upper", "=>", text.upper()
print "lower", "=>", text.lower()
print "split", "=>", text.split()
print "join", "=>", "+".join(text.split())
print "replace", "=>", text.replace("Python", "Perl")
print "find", "=>", text.find("Python"), text.find("Perl")
print "count", "=>", text.count("n")

## upper => MONTY PYTHON'S FLYING CIRCUS
## lower => monty python's flying circus
## split => ['Monty', "Python's", 'Flying', 'Circus']
## join => Monty+Python's+Flying+Circus
## replace => Monty Perl's Flying Circus
## find => 6 -1
## count => 3
