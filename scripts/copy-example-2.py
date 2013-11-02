import copy

a = [[1],[2],[3]]
b = copy.deepcopy(a)

print "before", "=>"
print a
print b

# modify original
a[0][0] = 0
a[1] = None

print "after", "=>"
print a
print b

## before =>
## [[1], [2], [3]]
## [[1], [2], [3]]
## after =>
## [[0], None, [3]]
## [[1], [2], [3]]
