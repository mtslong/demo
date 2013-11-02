import regsub

text = "Well, there's spam, egg, sausage and spam."

print regsub.sub("spam", "ham", text) # just the first
print regsub.gsub("spam", "bacon", text) # all of them

## Well, there's ham, egg, sausage and spam.
## Well, there's bacon, egg, sausage and bacon.
