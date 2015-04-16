import sys

# Try/Except for argv/c

try:
	name = sys.argv[1]
except IndexError, NameError:
	print "Usage: python something_useful.py <name>"
	name = 'World'


# Prints name

print "Hello", name




