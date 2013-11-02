import shutil
import os

SOURCE = "samples"
BACKUP = "samples-bak"

# create a backup directory
shutil.copytree(SOURCE, BACKUP)

print os.listdir(BACKUP)

# remove it
shutil.rmtree(BACKUP)

print os.listdir(BACKUP)

## ['sample.wav', 'sample.jpg', 'sample.au', 'sample.msg', 'sample.tgz',
## ...
## Traceback (most recent call last):
##  File "shutil-example-2.py", line 17, in ?
##    print os.listdir(BACKUP)
## os.error: No such file or directory
