import sys

def test(n):
    j = 0
    for i in range(n):
        j = j + i
    return n

def tracer(frame, event, arg):
    print event, frame.f_code.co_name, frame.f_lineno, "->", arg
    return tracer

# tracer is activated on the next call, return, or exception
sys.settrace(tracer)

# trace this function call
test(1)

# disable tracing
sys.settrace(None)

# don't trace this call
test(2)

## call test 3 -> None
## line test 3 -> None
## line test 4 -> None
## line test 5 -> None
## line test 5 -> None
## line test 6 -> None
## line test 5 -> None
## line test 7 -> None
## return test 7 -> 1
