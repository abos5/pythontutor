"""Kant Generator for Python

Generates mock philosophy based on a context-free grammar

Usage: python kgp.py [options] [source]

Options:
  -g ..., --grammar=...   use specified grammar file or URL
  -h, --help              show this help
  -d                      show debugging information while parsing
Examples:
  kgp.py                  generates several paragraphs of Kantian philosophy
  kgp.py -g husserl.xml   generates several paragraphs of Husserl
  kpg.py "<xref id='paragraph'/>"  generates a paragraph of Kant
  kgp.py template.xml     reads from template.xml to decide what to generate
"""

from xml.dom import minidom
import random
import toolbox
import sys
import getopt

_debug = 0


class NoSourceError(Exception):
    pass


class KantGenerator(object):
    """ generates mock philosophy based on a context-free grammar"""

    def __init__(self, grammar, source=None):
        self.loadGrammar(grammar)
        self.loadSource(source and source or self.getDefaultSource())
        self.refresh()

    def _load(self, source):
        """load XML input source, return parsed XML document

        - a URL of a remote XML file("http://diveintopython.org/kant.xml")
        - a filename of a local XML file ("path/to/kant.xml")
        - standard input("-")
        - the actual XML document, as a string
        """

        sock = toolbox.openAnything(source)
        xmldoc = minidom.parse(sock).documentElement
        sock.close()
        return xmldoc

    def loadGrammar(self, grammar):
        """load context-free grammar"""
        self.grammar = self._load(grammar)
        self.refs = {}
        for ref in self.grammar.getElementsByTagName('ref'):
            self.refs[ref.attributes["id"].value] = ref

    def loadSource(self, source):
        self.source = self._load(source)

    def getDefaultSource(self):
        """guess defualt source of the current grammar"""

        xrefs = {}
        for xref in self.grammar.getElementsByTagName("xrefs"):
            xrefs[xref.attributes["id"].value] = 1
        xrefs = xrefs.keys()
        standaloneXrefs = [e for e in self.refs.keys() if e not in xrefs]
        print(standaloneXrefs)
        if not standaloneXrefs:
            raise(NoSourceError, "can't guess source, and no source specified")
        return '<xref id="%s"/>' % random.choice(standaloneXrefs)

    def reset(self):
        """reset parser"""
        self.pieces = []
        self.capitalizeNextWord = 0

    def refresh(self):
        """reset output buffer, re-parse entire source file, and return output

        """
        self.reset()
        self.parse(self.source)
        return self.output()

    def output(self):
        """output generated text"""
        return "".join(self.pieces)

    def randomChildElement(self, node):
        choices = [e for e in node.childNodes if e.nodeType == e.ELEMENT_NODE]
        chosen = random.choice(choices)

        self.debug_log('%s available choices: %s\n' % (
            len(choices), [e.toxml() for e in choices]))
        self.debug_log('Chosen: %s\n' % chosen.toxml())
        return chosen

    def debug_log(self, msg):
        if _debug:
            sys.stderr.write(msg)

    def parse(self, node):
        parseMethod = getattr(self, "parse_%s" % node.__class__.__name__)
        parseMethod(node)

    def parse_Document(self, node):
        self.parse(node.documentElement)

    def parse_Text(self, node):
        text = node.data
        if self.capitalizeNextWord:
            self.pieces.append(text[0].upper())
            self.pieces.append(text[1:])
            self.capitalizeNextWord = 0
        else:
            self.pieces.append(text)

    def parse_Element(self, node):
        handlerMethod = getattr(self, 'do_%s' % node.tagName)
        handlerMethod(node)

    def parse_Comment(self, node):
        pass

    def parse_NoneType(self, node):
        pass

    def do_xref(self, node):
        """handle <xref id='...'> tag

        An <xref id='...'> tag is a cross-reference to a <ref id='...'>
        tag.  <xref id='sentence'/> evaluates to a randomly chosen child of
        <ref id='sentence'>.
        """
        id = node.attributes['id'].value
        self.parse(self.randomChildElement(self.refs[id]))

    def do_p(self, node):
        """handle <p> tag

        The <p> tag is the core of the grammar.  It can contain almost
        anything: freeform text, <choice> tags, <xref> tags, even other
        <p> tags.  If a "class='sentence'" attribute is found, a flag
        is set and the next word will be capitalized.  If a "chance='X'"
        attribute is found, there is an X% chance that the tag will be
        evaluated (and therefore a (100-X)% chance that it will be
        completely ignored)
        """
        keys = node.attributes.keys()

        if "class" in keys:
            if node.attributes["class"].value == "sentence":
                self.capitalizeNextWord = 1

        if "chance" in keys:
            chance = int(node.attributes['chance'].value)
            doit = (chance > random.randrange(100))
        else:
            doit = 1

        if doit:
            for child in node.childNodes:
                self.parse(child)

    def do_choice(self, node):
        self.parse(self.randomChildElement)


def usage():
    print(__doc__)


def main(argv):
    grammar = "kant.xml"
    try:
        opts, args = getopt.getopt(argv, "hg:d", ["help", "grammar="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "-help"):
            usage()
            sys.exit()

        elif opt == '-d':
            global _debug
            _debug = 1
        elif opt in ("-g", "-grammar"):
            grammar = arg

    source = "".join(args)
    k = KantGenerator(grammar, source)
    print(k.output())


if __name__ == "__main__":
    main(["-gkant.xml", 'kant_source.xml'])
    # main(sys.argv[1:])
    # print(sys.argv[1:])




# end of file
