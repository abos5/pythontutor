"""Regression testing framework

This module will search for scripts in the same directory named \
XYZtest.py. Each such script should be a test suit that tests a \
module through PyUnit.

"""
import sys
import os
import re
import unittest
from toolbox import exit


def regressionTest():
    path = os.path.abspath(os.path.dirname(sys.argv[0]))

    # obtain the required files
    files = os.listdir(path)
    test = re.compile('test\.py$', re.IGNORECASE)
    files = filter(test.search, files)

    # get rid of the extension
    filenameToModuleName = lambda f: os.path.splitext(f)[0]
    moduleNames = map(filenameToModuleName, files)
    modules = map(__import__, moduleNames)
    load = unittest.defaultTestLoader.loadTestsFromModule
    return unittest.TestSuite(map(load, modules))
    exit()


if __name__ == "__main__":
    unittest.main(defaultTest="regressionTest")

# end of file
