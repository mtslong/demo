import SimpleAsyncHTTP
import asyncore

class DummyConsumer:
    size = 0

    def http_header(self, request):
        # handle header
        if request.status is None:
            print "connection failed"
        else:
            print "status", "=>", request.status
            for key, value in request.header.items():
                print key, "=", value

    def feed(self, data):
        # handle incoming data
        self.size = self.size + len(data)

    def close(self):
        # end of data
        print self.size, "bytes in body"

#
# try it out

consumer = DummyConsumer()

request = SimpleAsyncHTTP.AsyncHTTP(
    "http://www.pythonware.com",
    consumer
    )

asyncore.loop()

## log: adding channel <AsyncHTTP  at 8e2850>
## status => ['HTTP/1.1', '200', 'OK\015\012']
## server = Apache/Unix (Unix)
## content-type = text/html
## content-length = 3730
## ...
## 3730 bytes in body
## log: closing channel 156:<AsyncHTTP connected at 8e2850>
