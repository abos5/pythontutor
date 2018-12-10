

class bar(object):

    def __str__(self):
        return "inst bar"


class foo(object):
    f = bar()

    def __init__(self):
        self.f = bar()

    def __bar(self):
        print(1)

    def bar(self):
        pass

    def __any(self):
        pass

    @staticmethod
    def b():
        print('static: b')

    @classmethod
    def c(self):
        print("class: c", self.f)

    def m(self):
        print("inst:  m", self.f)


f = foo()

f._foo__bar()
f.bar()

f.b()
foo.b()
f.c()
foo.c()
f.m()

print("--------------")
print("\n".join(dir(f)))



#eof
