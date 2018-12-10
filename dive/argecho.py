""" documentation of this file.
"""
# argecho.py
import sys
import getopt
for arg in sys.argv:
    print(arg)

_debug = 0


def usage():
    print(__doc__)
    print('---------')
    print('-- debug information ---')
    print('---------')


def main(argv):
    grammar = "kant.xml"
    try:
        opts, args = getopt.getopt(argv, "hg:d", [
            "help", "grammar=", "bad=", "grammer="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-d':
            global _debug
            _debug = 1
        elif opt in ("-g", "--grammar"):
            grammar = arg

    source = "".join(args)
    return source
    print(sys.argv[1:])
    print(grammar)

main(['-d', '-h', '--bad', 'something else', 'bad', 'asdsad'])

# end of file
