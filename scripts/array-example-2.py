import array

a = array.array("B", [1, 2, 3])

a.append(4)

a = a + a

a = a[2:-2]

print a
print repr(a.tostring())
for i in a:
    print i,

## array('B', [3, 4, 1, 2])
## '\003\004\001\002'
## 3 4 1 2
