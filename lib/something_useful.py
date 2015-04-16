import sys

# Try/Except for argv/c

try:
	name = sys.argv[1]
except IndexError:
	print "Usage: python something_useful.py <name>"


# Prints name

print "Hello", name




