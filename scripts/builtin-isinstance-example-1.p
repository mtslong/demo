class A:
    pass

class B:
    pass

class C(A):
    pass

class D(A, B):
    pass

def dump(object):
    print object, "=>",
    if isinstance(object, A):
        print "A",
    if isinstance(object, B):
        print "B",
    if isinstance(object, C):
        print "C",
    if isinstance(object, D):
        print "D",
    print

a = A()
b = B()
c = C()
d = D()

dump(a)
dump(b)
dump(c)
dump(d)
dump(0)
dump("string")

## <A instance at 8ca6d0> => A
## <B instance at 8ca750> => B
## <C instance at 8ca780> => A C
## <D instance at 8ca7b0> => A B D
## 0 =>
## string =>
