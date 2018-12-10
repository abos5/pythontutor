"""Miscellaneous utility functions"""
import sys

_debug = 1


def exit():
    if _debug:
        sys.exit()


def openAnything(source):
    """url, filename, or string -> stream

    Examples:
    >>> from xml.dom import minidom
    >>> sock = openAnything("http://localhost/kant.xml")
    >>> doc = minidom.parse(sock)
    >>> sock.close()
    >>> sock = openAnything("c:\\inetpub\\wwwroot\\kant.xml")
    >>> doc = minidom.parse(sock)
    >>> sock.close()
    >>> sock = openAnything("<ref id='conjunction'><text>and</text><text>or\
        </text>
        </ref>")
    >>> doc = minidom.parse(sock)
    """

    if hasattr(source, 'read'):
        return source

    if source == '-':
        return sys.stdin

    import urllib
    try:
        return urllib.urlopen(source)
    except (IOError, OSError):
        pass

    try:
        return open(source)
    except (IOError, OSError):
        pass

    import StringIO
    return StringIO.StringIO(str(source))



# end of file
