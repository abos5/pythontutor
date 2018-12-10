#! /usr/bin/python
import sys
import getopt

_debug = 0


def usage(err=False):
    print '''
    ssh:
        abos.space -option=value
    '''

    if err:
        print 'invalid argv!'


def main(argv):
    # retrive options
    try:
        opts, args = getopt.getopt(argv, "hg:d:", ["hey", ])
    except getopt.GetoptError:
        usage(True)
        sys.exit(2)

    # working on options
    for opt, arg in opts:
        if opt in ("-h", "-help"):
            usage()
            sys.exit()

        elif opt == '-d':
            global _debug
            _debug = 1
        elif opt in ("-g", "-grammar"):
            print arg


if __name__ == '__main__':
    argv = sys.argv
    argv.pop(0)
    main(sys.argv)

# sys.
# eof
