"""This file is to implement functions
with the same name and usage in php

"""


class Dump(object):
    """like var_dump in php
    """
    max_indent = 99

    def __init__(self, *content):
        assert hasattr(self, "output"), "Abstract output needs overide!"
        self.pieces = {}
        self.run(content)

    def run(self, content):
        self.distribute(content)
        self.output()

    def distribute(self, content):
        for i in range(len(content)):
            self.pieces[i] = self.analyze(content[i])

    def analyze(self, content):
        """ content(string, list, dict, tuple,int, unicode) -> tuple

        Return tuple has this possibilities:
        (typename, "This is a printable value")
        (typename, [
            (typename, "outputable"),
            (typename, "outputable")
        ])
        (typename, [
            (typename, [
                (typename, "outputable"),
                (typename, "outputable")
            ]),
        ])
        """
        typename = content.__class__.__name__
        try:
            method = getattr(self, "collect_%s" % typename)
        except AttributeError:
            return
        return (typename, method(content))

    def collect_dict(self, content):
        return [(k, self.analyze(v)) for k, v in content.items()]

    def collect_tuple(self, content):
        return self.collect_list(content)

    def collect_list(self, content):
        return [(
            k, self.analyze(content[k])) for k in range(len(content))]

    def collect_int(self, content):
        return content

    def collect_unicode(self, content):
        return content.encode('utf-8')

    def collect_str(self, content):
        return content


class DumpDefault(Dump):

    def output(self):
        self.indent = 0
        for k, arg in self.pieces.items():
            self.output_arg(arg, k)

    def output_arg(self, arg, key):
        t, v = arg
        blank_indent = self.get_indent()
        print("%s%s <%s>" % (blank_indent, key, t))
        self.indent += 1
        blank_indent = self.get_indent()
        if self.indent > self.max_indent:
            print("%s..." % blank_indent)
        elif v.__class__.__name__ == "list":
            for k, arg2 in v:
                self.output_arg(arg2, k)
        else:
            print("%s%s" % (blank_indent, v))
        self.indent -= 1

    def get_indent(self):
        if self.indent:
            return("\t" * self.indent)
        else:
            return ""


class DumpDoProcessOnly(Dump):
    def output(self):
        pass


class DumpDoNothing(DumpDoProcessOnly):

    def run(self, content):
        pass


var_dump = DumpDefault


def no_dump():
    global var_dump
    var_dump = DumpDoNothing

# end of file
