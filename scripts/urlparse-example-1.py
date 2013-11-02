import urlparse

print urlparse.urlparse("http://host/path;params?query#fragment")

## ('http', 'host', '/path', 'params', 'query', 'fragment')
