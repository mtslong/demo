import ConfigParser
import string

config = ConfigParser.ConfigParser()

config.read("samples/sample.ini")

# print summary
print
print string.upper(config.get("book", "title"))
print "by", config.get("book", "author"),
print  "(" + config.get("book", "email") + ")"
print
print config.get("ematter", "pages"), "pages"
print

# dump entire config file
for section in config.sections():
    print section
    for option in config.options(section):
        print " ", option, "=", config.get(section, option)

## THE PYTHON STANDARD LIBRARY
## by Fredrik Lundh (fredrik@pythonware.com)
##
## 250 pages
##
## book
##   title = Python Standard Library
##   email = fredrik@pythonware.com
##   author = Fredrik Lundh
##   version = 2.0-010504
##   __name__ = book
## ematter
##   __name__ = ematter
##   pages = 250
## hardcopy
##   __name__ = hardcopy
##   pages = 300
