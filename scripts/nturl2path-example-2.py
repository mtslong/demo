import urllib

file = r"c:\my\little\pony"

print urllib.pathname2url(file)
print urllib.url2pathname(urllib.pathname2url(file))

## ///C|/my/little/pony
## C:\my\little\pony
