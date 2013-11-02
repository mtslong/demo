import imaplib
import string, random
import StringIO, rfc822

SERVER = "imap.spam.egg"

USER  = "mulder"
PASSWORD = "trustno1"

# connect to server
server = imaplib.IMAP4(SERVER)

# login
server.login(USER, PASSWORD)
server.select()

# list items on server
resp, items = server.search(None, "ALL")
items = string.split(items[0])

# fetch a random item
id = random.choice(items)
resp, data = server.fetch(id, "(RFC822)")
text = data[0][1]

file = StringIO.StringIO(text)

message = rfc822.Message(file)

for k, v in message.items():
    print k, "=", v

print message.fp.read()

server.logout()

## subject = ANN: (the eff-bot guide to) The Standard Python Library
## message-id = <199910120816.KAA12177@larch.spam.egg>
## to = mulder@spam.egg
## date = Tue, 12 Oct 1999 10:16:19 +0200 (MET DST)
## from = <effbot@spam.egg>
## received = (effbot@spam.egg) by imap.algonet.se (8.8.8+Sun/8.6.12)
## id KAA12177 for effbot@spam.egg; Tue, 12 Oct 1999 10:16:19 +0200
## (MET DST)
##
## body text for test 5
