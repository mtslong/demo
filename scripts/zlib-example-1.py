import zlib

MESSAGE = "life of brian"

compressed_message = zlib.compress(MESSAGE)
decompressed_message = zlib.decompress(compressed_message)

print "original:", repr(MESSAGE)
print "compressed message:", repr(compressed_message)
print "decompressed message:", repr(decompressed_message)

## original: 'life of brian'
## compressed message: 'x\234\313\311LKU\310OSH*\312L\314\003\000!\010\004\302'
## decompressed message: 'life of brian'
