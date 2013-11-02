import pstats
import profile

def func1():
    for i in range(1000):
        pass

def func2():
    for i in range(1000):
        func1()

p = profile.Profile()
p.run("func2()")

s = pstats.Stats(p)
s.sort_stats("time", "name").print_stats()

##          1003 function calls in 1.574 CPU seconds
##
##    Ordered by: internal time, function name
##
##    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
##      1000    1.522    0.002    1.522    0.002 pstats-example-1.py:4(func1)
##         1    0.051    0.051    1.573    1.573 pstats-example-1.py:8(func2)
##         1    0.001    0.001    1.574    1.574 profile:0(func2())
##         1    0.000    0.000    1.573    1.573 <string>:1(?)
##         0    0.000             0.000          profile:0(profiler)
