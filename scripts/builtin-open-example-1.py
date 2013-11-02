def open(filename, mode="rb"):
    import __builtin__
    file = __builtin__.open(filename, mode)
    if file.read(5) not in("GIF87", "GIF89"):
        raise IOError, "not a GIF file"
    file.seek(0)
    return file

fp = open("samples/sample.gif")
print len(fp.read()), "bytes"

fp = open("samples/sample.jpg")
print len(fp.read()), "bytes"

## 3565 bytes
## Traceback (innermost last):
##   File "builtin-open-example-1.py", line 12, in ?
##   File "builtin-open-example-1.py", line 5, in open
## IOError: not a GIF file
