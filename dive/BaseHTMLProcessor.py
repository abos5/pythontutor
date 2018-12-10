from sgmllib import SGMLParser
import htmlentitydefs


class BaseHTMLProcessor(SGMLParser):
    def reset(self):
        self.pieces = []
        SGMLParser.reset(self)

    def unknown_starttag(self, tag, attrs):
        """
        attrs is a list of (attr, value) tuples
        e.g. for <pre class="screen">, tag="pre", attrs=[("class", "screen")]
        """
        starttrs = "".join(['%s="%s"' % (key, value) for key, value in attrs])
        self.pieces.append("<%(tag)s %(starttrs)s>" % locals())

    def unknown_endtag(self, tag):
        self.pieces.append("</%(tag)s>" % locals())

    def handle_charref(self, ref):
        self.pieces.append("&#%(ref)s;" % locals())

    def handle_entityref(self, ref):
        self.pieces.append("&#%(ref)s" % locals())

        if ref in htmlentitydefs.entitydefs:
            self.pieces.append(";")

    def handle_data(self, text):
        self.pieces.append(text)

    def handle_comment(self, text):
        self.pieces.append("<!-%(text)s->" % locals())

    def handle_pi(self, text):
        self.pieces.append("<?%(text)s>" % locals())

    def handle_decl(self, text):
        self.pieces.append("<!%(text)s>" % locals())

    def output(self):
        """Return processed HTML as a single string"""

        return "".join(self.pieces)


# end of file
