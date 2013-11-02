import shutil
import os

for file in os.listdir("."):
    if os.path.splitext(file)[1] == ".py":
        print file
        shutil.copy(file, os.path.join("backup", file))

## aifc-example-1.py
## anydbm-example-1.py
## array-example-1.py
## ...
