import urllib

fp = urllib.urlopen("http://www.python.org")

op = open("out.html", "wb")

n = 0

while 1:
    s = fp.read(8192)
    if not s:
        break
    op.write(s)
    n = n + len(s)

fp.close()
op.close()

for k, v in fp.headers.items():
    print k, "=", v

print "copied", n, "bytes from", fp.url

## server = Apache/1.3.6 (Unix)
## content-type = text/html
## accept-ranges = bytes
## date = Mon, 11 Oct 1999 20:11:40 GMT
## connection = close
## etag = "741e9-7870-37f356bf"
## content-length = 30832
## last-modified = Thu, 30 Sep 1999 12:25:35 GMT
## copied 30832 bytes from http://www.python.org
