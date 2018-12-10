import sys

# %d  digit
# %i  int
# %o  oX 8
# %u  number
# %x  OX 16
# %X  16 in capital
# %e  1.000000e+00
# %E  1.000000E+00
# %f  float
# %F  float
# %g  small float?
# %G  small float?
# %c  char?
# %r raw data
# %s   string
# %% => "%"
# %- 30s align to left with an space padded to 30 length
#

print('\\ %s' % "some thing nice \\\\")
print('\' %s' % "some thing nice \\'")
print('\" %s' % "some thing nice \\\"")
print('\a %s' % "some thing nice \\a")
print('\b %s' % "some thing nice \\b")
print('\f %s' % "some thing nice \\f")
print('\n %s' % "some thing nice \\n")
print('\r %s' % "some thing nice \\r")
print('\t %s' % "some thing nice \\t")
print('\v %s' % "some thing nice \\v")

rs = filter(lambda x: x % 2 == 1, [3, 4, 5])
print(rs)

rs = reduce(lambda x, y: x * y, [3, 4, 5])
print(rs)

rs = map(lambda x: x ** 3, [1, 4, 5])
print(rs)

fname = "l(%d)"
l = lambda x: x * 2
rs = eval(fname % 3)

print(l(3))
print(rs)

dict1 = {1: 2, 3: 4, 5: 6}
dict2 = {1: 2, 3: 4, 5: 6}
print(dict1 == dict2)
print(dict1 is dict2)

sys.exit()

# try except finally


def cause_error(msg):
    print(msg)
    print(msg.awesome)


try:
    print(1)
    print(2)
    cause_error("info")
    raise(AssertionError("my own error"))
    dict1 = {
        "a": "b",
        "b": "c",
        "c": "d",
        "d": "e",
    }
    print(dict1.length)
    print(dict1['e'])
    print(dict1.replace)
    assert False
# stop error from exiting program
except AssertionError, e:
    print("why would this assert wrong? %s" % e[0])
except AttributeError, e:
    print("Error: %s" % e[0])
except KeyError:
    print("some real stupid attribute error")
# will exe whatever an error  occured.
finally:
    print("People ain't saint, and they make mistakes.")

print(2)

print("Here I am, every body.")
print("Life goes on.")


sys.exit()




# yield
def fab(max):
    n = 0
    while n < max:
        x = n
        yield n
        print("%d once" % x)
        n = n + 1
        yield n
        print("%d twice" % x)
        if n == 5:
            return
        if n > 3:
            yield n
            print("%d third" % x)

for a in fab(10):
    pass
