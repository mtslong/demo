import zlib
import glob

for file in glob.glob("samples/*"):

    indata = open(file, "rb").read()
    outdata = zlib.compress(indata, zlib.Z_BEST_COMPRESSION)

    print file, len(indata), "=>", len(outdata),
    print "%d%%" % (len(outdata) * 100 / len(indata))

## samples\sample.au 1676 => 1109 66%
## samples\sample.gz 42 => 51 121%
## samples\sample.htm 186 => 135 72%
## samples\sample.ini 246 => 190 77%
## samples\sample.jpg 4762 => 4632 97%
## samples\sample.msg 450 => 275 61%
## samples\sample.sgm 430 => 321 74%
## samples\sample.tar 10240 => 125 1%
## samples\sample.tgz 155 => 159 102%
## samples\sample.txt 302 => 220 72%
## samples\sample.wav 13260 => 10992 82%
