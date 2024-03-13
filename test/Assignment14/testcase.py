import unittest

from src.Assignment14.util import find_happiness
class MyTestCase(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(1, find_happiness())  # 3 2\n1 5 3\n3 1\n5 7

    def testcase2(self):
        self.assertEqual(1, find_happiness())  # 5 5\n999999991 999999992 999999993 999999994 999999999\n999999991 999999993 999999995 999999999 999999997\n999999990 999999992 999999996 999999998 999999994

if __name__ == '__main__':
    unittest.main()
