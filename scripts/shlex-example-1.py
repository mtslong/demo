import shlex

lexer = shlex.shlex(open("samples/sample.netrc", "r"))
lexer.wordchars = lexer.wordchars + "._"

while 1:
    token = lexer.get_token()
    if not token:
        break
    print repr(token)

## 'machine'
## 'secret.fbi'
## 'login'
## 'mulder'
## 'password'
## 'trustno1'
## 'machine'
## 'non.secret.fbi'
## 'login'
## 'scully'
## 'password'
## 'noway'
