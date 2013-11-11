import array

a = array.array("B", range(16)) # unsigned char
b = array.array("h", range(16)) # signed short

print a
print repr(a.tostring())

print b
print repr(b.tostring())

## array('B', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
## '\000\001\002\003\004\005\006\007\010\011\012\013\014\015\016\017'
## array('h', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
## '\000\000\001\000\002\000\003\000\004\000\005\000\006\000\007\000
## \010\000\011\000\012\000\013\000\014\000\015\000\016\000\017\000'