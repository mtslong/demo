import sndhdr

result = sndhdr.what("samples/sample.wav")

if result:
    print "file format:", result
else:
    print "cannot identify file"

## file format: ('wav', 44100, 1, -1, 16)
