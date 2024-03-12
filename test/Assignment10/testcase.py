import unittest
from src.Assignment10.util import floor_ceil_rint

class MyTestCase(unittest.TestCase):
    def testcase1(self):
        self.assertEqual("[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]\n[  2.   3.   4.   5.   6.   7.   8.   9.  10.]\n[  1.   2.   3.   4.   6.   7.   8.   9.  10.]", floor_ceil_rint("1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9"))  # add assertion here

    def testcase2(self):
        self.assertEqual("[ 2.  3.  4.  5.  6.  7.  8.]\n[ 3.  4.  5.  6.  7.  8.  9.]\n[ 2.  3.  4.  6.  7.  8.  9.]", floor_ceil_rint("2.2 3.3 4.4 5.5 6.6 7.7 8.8"))  # add assertion here

if __name__ == '__main__':
    unittest.main()
