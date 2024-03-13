import unittest
from src.Assignment16.util import piling_up

class MyTestCase(unittest.TestCase):
    def testcase1(self):
        self.assertEqual("Yes\nNo", piling_up())

    def testcase2(self):
        self.assertEqual("Yes", piling_up())

if __name__ == '__main__':
    unittest.main()
