import unittest
from src.Assignment7.util import calendar_module

class MyTestCase(unittest.TestCase):
    def testcase1(self):
        self.assertEqual("WEDNESDAY", calendar_module("08 05 2015"))

    def testcase2(self):
        self.assertEqual("FRIDAY", calendar_module("04 06 2012"))

    def testcase3(self):
        self.assertEqual("SATURDAY", calendar_module("02 13 2010"))


if __name__ == '__main__':
    unittest.main()
