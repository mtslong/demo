import zipfile

file = zipfile.ZipFile("samples/sample.zip", "r")

for name in file.namelist():
    data = file.read(name)
    print name, len(data), repr(data[:10])

## sample.txt 302 'We will pe'
## sample.jpg 4762 '\377\330\377\340\000\020JFIF'
