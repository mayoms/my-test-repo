import sys
from greeter import Greeter

# Try/Except for argv/c

try:
	name = sys.argv[1]
except IndexError, NameError:
	print "Usage: python something_useful.py <name>"
	name = 'World'


greeter = Greeter(name)
# Prints name

print greeter.greet()




