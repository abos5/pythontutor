
import unittest
import re


class Plural1Works(unittest.TestCase):

    knownValues = {
        "apple": "apples",
        "pear": "pears",
    }

    def testPlural1(self):
        """known values should be translated equals"""
        import plural1
        self.baseTranslate(plural1.plural)

    def testPlural2(self):
        """known values should be translated equals in plural2"""
        import plural2
        self.baseTranslate(plural2.plural)

    def testPlural3(self):
        """known values should be translated equals in plural3"""
        import plural3
        self.baseTranslate(plural3.plural)

    def testPlural4(self):
        """known values should be translated equals in plural4"""
        import plural4
        self.baseTranslate(plural4.plural)

    def testPlural5(self):
        """known values should be translated equals in plural5"""
        import plural5
        self.baseTranslate(plural5.plural)

    def testPlural6(self):
        """known values should be translated equals in plural6"""
        import plural6
        self.baseTranslate(plural6.plural)

    def baseTranslate(self, translateMethod):

        for word in self.knownValues:
            expected = self.knownValues[word]
            self.assertEquals(expected, translateMethod(word))

    def testFoo(self):
        """trying out re methods"""

        self.assertEquals('Mork', re.sub('[a]', 'o', 'Mark'))

if __name__ == "__main__":
    unittest.main()

# end of file
