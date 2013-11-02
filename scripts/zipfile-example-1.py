import zipfile

file = zipfile.ZipFile("samples/sample.zip", "r")

# list filenames
for name in file.namelist():
    print name,
print

# list file information
for info in file.infolist():
    print info.filename, info.date_time, info.file_size

## sample.txt sample.jpg
## sample.txt (1999, 9, 11, 20, 11, 8) 302
## sample.jpg (1999, 9, 18, 16, 9, 44) 4762
