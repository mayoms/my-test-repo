import sys

try:
	name = sys.argv[1]
except IndexError:
	name = 'Micah'

print "Hello", name

