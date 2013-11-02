try:
    import cPickle
    pickle = cPickle
except ImportError:
    import pickle

class Sample:
    def __init__(self, value):
        self.value = value

sample = Sample(1)

data = pickle.dumps(sample)

print pickle
print repr(data)

## <module 'cPickle' (built-in)>
## "(i__main__\012Sample\012p1\012(dp2\012S'value'\012p3\012I1\012sb."

