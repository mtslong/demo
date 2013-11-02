import getpass

usr = getpass.getuser()

pwd = getpass.getpass("enter password for user %s: " % usr)

print usr, pwd

## enter password for user mulder:
## mulder trustno1
