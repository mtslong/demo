def dump(function):
    if callable(function):
        print function, "is callable"
    else:
        print function, "is *not* callable"

class A:
    def method(self, value):
        return value

class B(A):
    def __call__(self, value):
        return value

a = A()
b = B()

dump(0) # simple objects
dump("string")
dump(callable)
dump(dump) # function

dump(A) # classes
dump(B)
dump(B.method)

dump(a) # instances
dump(b)
dump(b.method)

## 0 is *not* callable
## string is *not* callable
## <built-in function callable> is callable
## <function dump at 8ca320> is callable
## A is callable
## B is callable
## <unbound method A.method> is callable
## <A instance at 8caa10> is *not* callable
## <B instance at 8cab00> is callable
## <method A.method of B instance at 8cab00> is callable
