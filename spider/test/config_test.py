from nose.tools import assert_equal
import config.main
import os.path


# class ConfigTest(unittest.TestCase):

def testPaths():
    """Every defined path should exist"""
    for path in config.main.paths:
        assert(os.path.exists(config.main.paths[path]))

# end of file
