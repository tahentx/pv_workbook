# print("Hello".format)
# two = "Hello, {}".format("Todd")
# three = "{} {} {}".format("Yo", "hi", "what up")
# four = "{2} {0} {1}".format("Yo", "hi", "what up")
# five = "{a} {b} {c}".format(a="Joe", b="Chuck", c="Steve")

import sys

print("Name of the script : {}".format(sys.argv[0]))
print("Arguments of the script : {}".format(sys.argv[1:]))
