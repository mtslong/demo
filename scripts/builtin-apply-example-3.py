class Rectangle:
    def __init__(self, color="white", width=10, height=10):
        print "create a", color, self, "sized", width, "x", height

class RoundedRectangle(Rectangle):
    def __init__(self, **kw):
        apply(Rectangle.__init__, (self,), kw)

rect = Rectangle(color="green", height=100, width=100)
rect = RoundedRectangle(color="blue", height=20)

## create a green <Rectangle instance at 8c8260> sized 100 x 100
## create a blue <RoundedRectangle instance at 8c84c0> sized 10 x 20
