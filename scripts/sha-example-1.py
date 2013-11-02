import sha

hash = sha.new()
hash.update("spam, spam, and eggs")

print repr(hash.digest())
print hash.hexdigest()

## '\321\333\003\026I\331\272-j\303\247\240\345\343Tvq\364\346\311'
## d1db031649d9ba2d6ac3a7a0e5e3547671f4e6c9
