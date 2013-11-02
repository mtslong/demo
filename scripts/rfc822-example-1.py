import rfc822

file = open("samples/sample.eml")

message = rfc822.Message(file)

for k, v in message.items():
    print k, "=", v

print len(file.read()), "bytes in body"

## subject = Re: python library book!
## from = "Frank" <your@editor>
## message-id = <20001114144603.00abb310@oreilly.com>
## to = "Fredrik Lundh" <fredrik@effbot.org>
## date = Tue, 14 Nov 2000 14:55:07 -0500
## 25 bytes in body
