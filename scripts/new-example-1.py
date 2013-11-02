import new

class Sample:

    a = "default"

    def __init__(self):
        self.a = "initialised"

    def __repr__(self):
        return self.a

#
# create instances

a = Sample()
print "normal", "=>", a

b = new.instance(Sample, {})
print "new.instance", "=>", b

b.__init__()
print "after __init__", "=>", b

c = new.instance(Sample, {"a": "assigned"})
print "new.instance w. dictionary", "=>", c

## normal => initialised
## new.instance => default
## after __init__ => initialised
## new.instance w. dictionary => assigned
