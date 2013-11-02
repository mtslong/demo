import array

a = array.array("i", "fish license") # signed integer

print a
print repr(a.tostring())
print a.tolist()

## array('i', [1752394086, 1667853344, 1702063717])
## 'fish license'
## [1752394086, 1667853344, 1702063717]
