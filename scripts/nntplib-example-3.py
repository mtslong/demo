import nntplib
import string, random
import StringIO, rfc822

SERVER = "news.spam.egg"
GROUP  = "comp.lang.python"

# connect to server
server = nntplib.NNTP(SERVER)

resp, count, first, last, name = server.group(GROUP)
for i in range(10):
    try:
        id = random.randint(int(first), int(last))
        resp, id, message_id, text = server.article(str(id))
    except (nntplib.error_temp, nntplib.error_perm):
        pass # no such message (maybe it was deleted?)
    else:
        break # found a message!
else:
    raise SystemExit

text = string.join(text, "\n")
file = StringIO.StringIO(text)

message = rfc822.Message(file)

for k, v in message.items():
    print k, "=", v

print message.fp.read()

## mime-version = 1.0
## content-type = text/plain; charset="iso-8859-1"
## message-id = <008501bf1417$1cf90b70$f29b12c2@sausage.spam.egg>
## lines = 22
## ...
## from = "Fredrik Lundh" <fredrik@pythonware.com>
## nntp-posting-host = parrot.python.org
## subject = ANN: (the eff-bot guide to) The Standard Python Library
## ...
## </F>
