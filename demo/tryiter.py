

class Foo(object):

    def __iter__(self):
        for i in range(100):
            yield i

    __str__ = __iter__

hot = Foo()


def bar():
    for i in range(10):
        yield i


for i in bar():
    print(i)

#eof
