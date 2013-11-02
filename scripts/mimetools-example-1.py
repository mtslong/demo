import mimetools

file = open("samples/sample.msg")

msg = mimetools.Message(file)

print "type", "=>", msg.gettype()
print "encoding", "=>", msg.getencoding()
print "plist", "=>", msg.getplist()

print "header", "=>"
for k, v in msg.items():
    print "  ", k, "=", v

## type => text/plain
## encoding => 7bit
## plist => ['charset="iso-8859-1"']
## header =>
##    mime-version = 1.0
##    content-type = text/plain;
##  charset="iso-8859-1"
##    to = effbot@spam.egg
##    date = Fri, 15 Oct 1999 03:21:15 -0400
##    content-transfer-encoding = 7bit
##    from = "Fredrik Lundh" <fredrik@pythonware.com>
##    subject = By the way...
## ...
