import mailcap

caps = mailcap.getcaps()

for k, v in caps.items():
    print k, "=", v

## image/* = [{'view': 'pilview'}]
## application/postscript = [{'view': 'ghostview'}]
