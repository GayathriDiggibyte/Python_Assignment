import unittest
from src.Assignment17.util import find_probability

class MyTestCase(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(0.833333333333, find_probability()) # 4 a a c d 2

    def testcase2(self):
        self.assertEqual(0.000000000000, find_probability()) #10 b b b b b h h j k f 10

if __name__ == '__main__':
    unittest.main()
