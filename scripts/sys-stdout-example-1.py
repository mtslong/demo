import sys
import string

class Redirect:

    def __init__(self, stdout):
        self.stdout = stdout

    def write(self, s):
        self.stdout.write(string.lower(s))

# redirect standard output (including the print statement)
old_stdout = sys.stdout
sys.stdout = Redirect(sys.stdout)

print "HEJA SVERIGE",
print "FRISKT HUM÷R"

# restore standard output
sys.stdout = old_stdout

print "M≈≈≈≈L!"

## heja sverige friskt humˆr
## M≈≈≈≈L!
