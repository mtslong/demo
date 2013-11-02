import md5
import string, random

def getchallenge():
    # generate a 16-byte long random string.  (note that the built-
    # in pseudo-random generator uses a 24-bit seed, so this is not
    # as good as it may seem...)
    challenge = map(lambda i: chr(random.randint(0, 255)), range(16))
    return string.join(challenge, "")

def getresponse(password, challenge):
    # calculate combined digest for password and challenge
    m = md5.new()
    m.update(password)
    m.update(challenge)
    return m.digest()

#
# server/client communication

# 1. client connects.  server issues challenge.

print "client:", "connect"

challenge = getchallenge()

print "server:", repr(challenge)

# 2. client combines password and challenge, and calculates
# the response

client_response = getresponse("trustno1", challenge)

print "client:", repr(client_response)

# 3. server does the same, and compares the result with the
# client response.  the result is a safe login in which the
# password is never sent across the communication channel.

server_response = getresponse("trustno1", challenge)

if server_response == client_response:
    print "server:", "login ok"

## client: connect
## server: '\334\352\227Z#\272\273\212KG\330\265\032>\311o'
## client: "l'\305\240-x\245\237\035\225A\254\233\337\225\001"
## server: login ok
