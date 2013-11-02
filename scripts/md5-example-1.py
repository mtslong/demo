import md5

hash = md5.new()
hash.update("spam, spam, and eggs")

print repr(hash.digest())

## 'L\005J\243\266\355\243u`\305r\203\267\020F\303'
