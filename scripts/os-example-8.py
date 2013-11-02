import os

if os.name == "nt":
    command = "dir"
else:
    command = "ls -l"

os.system(command)
    
## -rwxrw-r--   1 effbot  effbot        76 Oct  9 14:17 README
## -rwxrw-r--   1 effbot  effbot      1727 Oct  7 19:00 SimpleAsyncHTTP.py
## -rwxrw-r--   1 effbot  effbot       314 Oct  7 20:29 aifc-example-1.py
## -rwxrw-r--   1 effbot  effbot       259 Oct  7 20:38 anydbm-example-1.py
## ...
