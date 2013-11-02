import grp
import os

print grp.getgrgid(os.getgid())
print grp.getgrnam("wheel")

## ('effbot', '', 4711, ['effbot'])
## ('wheel', '', 10, ['root', 'effbot', 'gorbot', 'timbot'])
