import base64, sys

if not sys.argv[1:]:
    print "Usage: gif2tk.py giffile >pyfile"
    sys.exit(1)

data = open(sys.argv[1], "rb").read()

if data[:4] != "GIF8":
    print sys.argv[1], "is not a GIF file"
    sys.exit(1)

print '# generated from', sys.argv[1], 'by gif2tk.py'
print
print 'from Tkinter import PhotoImage' 
print
print 'image = PhotoImage(data="""'
print base64.encodestring(data),
print '""")'

## # generated from samples/sample.gif by gif2tk.py
##
## from Tkinter import PhotoImage
##
## image = PhotoImage(data="""
## R0lGODlhoAB4APcAAAAAAIAAAACAAICAAAAAgIAAgACAgICAgAQEBIwEBIyMBJRUlISE/LRUBAQE
## ...
## AjmQBFmQBnmQCJmQCrmQDNmQDvmQEBmREnkRAQEAOw==
## """)
