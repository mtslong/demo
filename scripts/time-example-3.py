import time

t0 = time.time()
tm = time.localtime(t0)

print tm

print t0
print time.mktime(tm)

## (1999, 9, 9, 0, 11, 8, 3, 252, 1)
## 936828668.16
## 936828668.0
