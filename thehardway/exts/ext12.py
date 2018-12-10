import os.path
fl = open(__file__)

print type(fl)
str1 = fl.readline()
while not str1 == '':
    str1 = fl.readline()
    print str1,

name = raw_input("Name? ")
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How heavy are you? ")

print "So, %s, you are %r old, %r tall and %r heavy." % (name, age, height, weight)
