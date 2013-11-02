import mimetypes
import glob, urllib

for file in glob.glob("samples/*"):
    url = urllib.pathname2url(file)
    print file, mimetypes.guess_type(url)

## samples\sample.au ('audio/basic', None)
## samples\sample.ini (None, None)
## samples\sample.jpg ('image/jpeg', None)
## samples\sample.msg (None, None)
## samples\sample.tar ('application/x-tar', None)
## samples\sample.tgz ('application/x-tar', 'gzip')
## samples\sample.txt ('text/plain', None)
## samples\sample.wav ('audio/x-wav', None)
## samples\sample.zip ('application/zip', None)
