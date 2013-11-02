class A:
    def a(self):
        pass
    def b(self):
        pass

class B(A):
    def c(self):
        pass
    def d(self):
        pass

def getmembers(klass, members=None):
    # get a list of all class members, ordered by class
    if members is None:
        members = []
    for k in klass.__bases__:
        getmembers(k, members)
    for m in dir(klass):
        if m not in members:
            members.append(m)
    return members

print getmembers(A)
print getmembers(B)
print getmembers(IOError)

## ['__doc__', '__module__', 'a', 'b']
## ['__doc__', '__module__', 'a', 'b', 'c', 'd']
## ['__doc__', '__getitem__', '__init__', '__module__', '__str__']
