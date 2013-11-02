import reconvert

for pattern in "abcd", "a\(b*c\)d", "\<\w+\>":
    print pattern, "=>", reconvert.convert(pattern)

## abcd => abcd
## a\(b*c\)d => a(b*c)d
## \<\w+\> => \b\w+\b
