import soundex

a = "fredrik"
b = "friedrich"

print soundex.get_soundex(a), soundex.get_soundex(b)
print soundex.sound_similar(a, b)

## F63620 F63620
## 1
