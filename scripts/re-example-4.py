import re

text = "you're no fun anymore..."

# literal replace (string.replace is faster)
print re.sub("fun", "entertaining", text)

# collapse all non-letter sequences to a single dash
print re.sub("[^\w]+", "-", text)

# convert all words to beeps
print re.sub("\S+", "-BEEP-", text)

## you're no entertaining anymore...
## you-re-no-fun-anymore-
## -BEEP- -BEEP- -BEEP- -BEEP-
