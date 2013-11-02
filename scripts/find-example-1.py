import find

# find all JPEG files in or beneath the current directory
for file in find.find("*.jpg", "."):
    print file

## .\samples\sample.jpg
