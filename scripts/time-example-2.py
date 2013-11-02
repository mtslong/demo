import time

now = time.localtime(time.time())

print time.asctime(now)
print time.strftime("%y/%m/%d %H:%M", now)
print time.strftime("%a %b %d", now)
print time.strftime("%c", now)
print time.strftime("%I %p", now)
print time.strftime("%Y-%m-%d %H:%M:%S %Z", now)

# do it by hand...
year, month, day, hour, minute, second, weekday, yearday, daylight = now
print "%04d-%02d-%02d" % (year, month, day)
print "%02d:%02d:%02d" % (hour, minute, second)
print ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")[weekday], yearday

## Sun Oct 10 21:39:24 1999
## 99/10/10 21:39
## Sun Oct 10
## Sun Oct 10 21:39:24 1999
## 09 PM
## 1999-10-10 21:39:24 CEST
## 1999-10-10
## 21:39:24
## SUN 283
