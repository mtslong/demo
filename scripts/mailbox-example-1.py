import mailbox

mb = mailbox.UnixMailbox(open("/var/spool/mail/effbot"))

while 1:
    msg = mb.next()
    if not msg:
        break
    for k, v in msg.items():
        print k, "=", v
    body = msg.fp.read()
    print len(body), "bytes in body"

## subject = for he's a ...
## message-id = <199910150027.CAA03202@spam.egg>
## received = (from fredrik@pythonware.com)
##  by spam.egg (8.8.7/8.8.5) id CAA03202
##  for effbot; Fri, 15 Oct 1999 02:27:36 +0200
## from = Fredrik Lundh <fredrik@pythonware.com>
## date = Fri, 15 Oct 1999 12:35:36 +0200
## to = effbot@spam.egg
## 1295 bytes in body
