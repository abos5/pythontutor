""" index file

"""
import config
import getopt
import sys

# print(getopt.getopt(argv))

sys.argv = ['', '-p', 'asd', '-g', 'ddd', ]


def usage():
    print(__doc__)

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hp:g:')
    except getopt.GetoptError:
        usage()
        sys.exit()
    project = [arg for opt, arg in opts if opt == '-p'][0]

    # print(options)
    spy = config.Spy()
    spy.run()


# end of file
