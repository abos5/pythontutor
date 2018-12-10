from sys import exit


class Thing(object):
    """
    In Python,
    if a property haven't got modified in an instance, then
    it refers to the property instead of the address of the property
    """
    prop = {1: 2}
    prop2 = 10001
    prop3 = 2
    prop4 = 3

    def say(self):
        print self.prop2


a = Thing()
a.prop2 = 2
b = Thing()
print getattr(b, 'say')()
print id(Thing.prop2)
print id(a.prop)
print id(Thing.prop)
Thing.prop = {2: 3}
print id(a.prop)
print id(Thing.prop)
print a.prop is Thing.prop  # True
a.prop = {1: 2}
print id(a.prop)
print id(Thing.prop)
print a.prop is Thing.prop  # False

exit(0)


stuff = ['Test', 'This', "Out"]
print ' '.join(stuff)

a = 1
e = 1.0
b = 1
c = 's'
d = 's'
print id(a)
print id(e)
print id(b)
print id(c)
print id(d)


print a is b
print c is d
print "----------"


class TheThing(object):

    static = 0
    this = None

    def __init__(self):
        self.number = 0
        # self.static = 0
        global TheThing
        self.this = TheThing

    def some_function(self):
        print "I got called."

    def add_me_up(self, more):
        self.number += more
        return self.number

    def add_static_up(self, more):
        self.this.static += more
        return self.this.static

#two different things

a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print a.add_me_up(20)
print b.add_me_up(20)
print TheThing.static

print "static of a is %u" % a.static
print a.add_static_up(10)
print "static of The is %u" % TheThing.static
TheThing.static = 30

print "static of a is %u" % a.static
print b.add_static_up(10)
print "static of b is %u" % b.static
print "static of The is %u" % TheThing.static

#end of file
