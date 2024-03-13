import unittest
from src.Assignment15.util import order_words

class MyTestCase(unittest.TestCase):
    def testcase1(self):
        self.assertEqual("3\n2 1 1 ", order_words())  # 4 bcdef abcdefg bcde bcdef

    def testcase2(self):
        self.assertEqual("2\n2 2 ", order_words())  # 1000 a a a...
if __name__ == '__main__':
    unittest.main()
