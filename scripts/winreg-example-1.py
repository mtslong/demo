import _winreg

explorer = _winreg.OpenKey(
    _winreg.HKEY_CURRENT_USER,
    "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer"
    )

# list values owned by this registry key
try:
    i = 0
    while 1:
        name, value, type = _winreg.EnumValue(explorer, i)
        print repr(name),
        i += 1
except WindowsError:
    print

value, type =_winreg.QueryValueEx(explorer, "Logon User Name")

print
print "user is", repr(value)

## 'Logon User Name' 'CleanShutdown' 'ShellState' 'Shutdown Setting'
## 'Reason Setting' 'FaultCount' 'FaultTime' 'IconUnderline' ...
##
## user is u'Effbot'
