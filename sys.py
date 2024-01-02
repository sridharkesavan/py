import sys

"""
# Simple sys.argv that needs atleast 1 argument
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
"""

"""
# Incase an argument is not paased it throws an exception message
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1])
"""

"""
# exits the condition if argument is less than expected

print("Hello, my name is", sys.argv[1])
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1])
"""

"""
# Produces a bug ie prints the name of the file as well
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("Hello, my name is", arg)
"""

#introducing slice to remove the first argument(name of the file)

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)