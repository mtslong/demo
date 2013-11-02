import ftplib
import sys

def gettext(ftp, filename, outfile=None):
    # fetch a text file
    if outfile is None:
        outfile = sys.stdout
    # use a lambda to add newlines to the lines read from the server
    ftp.retrlines("RETR " + filename, lambda s, w=outfile.write: w(s+"\n"))

def getbinary(ftp, filename, outfile=None):
    # fetch a binary file
    if outfile is None:
        outfile = sys.stdout
    ftp.retrbinary("RETR " + filename, outfile.write)

ftp = ftplib.FTP("www.python.org")
ftp.login("anonymous", "ftplib-example-2")

gettext(ftp, "README")
getbinary(ftp, "welcome.msg")

## WELCOME to python.org, the Python programming language home site.
##
## You are number %N of %M allowed users.  Ni!
##
## Python Web site: http://www.python.org/
##
## CONFUSED FTP CLIENT?  Try begining your login password with '-' dash.
## This turns off continuation messages that may be confusing your client.
## ...
