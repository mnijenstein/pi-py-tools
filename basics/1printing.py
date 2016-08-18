###comments go like this###
print "Hello"

print "4/7", 4/7
print "4.0/7", 4.0/7
print "4/7.0", 4/7.0

print "3+2<5-7", 3+2<5-7

###Print formatted variables###
var1 = 'Text'
var2 = 25.0

print "Formatted text. \n var1: %s, var2d: %d, var2f: %f" % (var1, var2, var2)

###More printing examples###
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# %r = raw
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
print "#"*10

print "some",
print "other"

formatter="%r %r"
print "formatters: ",formatter % (formatter, formatter)

print """
Text and 
stuff
"""

print "Input value:"
var3 = raw_input()
var4 = raw_input("input value:")
