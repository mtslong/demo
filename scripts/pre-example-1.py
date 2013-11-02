import pre

p = pre.compile("[Python]+")

print p.findall("Python is not that bad")

## ['Python', 'not', 'th', 't']

