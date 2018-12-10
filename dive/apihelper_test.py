import apihelper
import unittest


class FooWorks(unittest.TestCase):

    def testFoo(self):
        b = 'a'
        self.assertEquals('a', b)

    def testInfo(self):
        info = apihelper.info
        self.assertEquals(info, apihelper.info)

# end of file
