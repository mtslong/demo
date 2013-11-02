import urlparse

base = "http://spam.egg/my/little/pony"

for path in "/index", "goldfish", "../black/cat":
    print path, "=>", urlparse.urljoin(base, path)

## /index => http://spam.egg/index
## goldfish => http://spam.egg/my/little/goldfish
## ../black/cat => http://spam.egg/my/black/cat
