import profile

def func1():
    for i in range(1000):
        pass

def func2():
    for i in range(1000):
        func1()

profile.run("func2()")

##      1003 function calls in 2.380 CPU seconds
##
## Ordered by: standard name
##
## ncalls tottime percall cumtime percall filename:lineno(function)
##      1   0.000   0.000   2.040   2.040 <string>:1(?)
##   1000   1.950   0.002   1.950   0.002 profile-example-1.py:3(func1)
##      1   0.090   0.090   2.040   2.040 profile-example-1.py:7(func2)
##      1   0.340   0.340   2.380   2.380 profile:0(func2())
##      0   0.000           0.000         profile:0(profiler)
