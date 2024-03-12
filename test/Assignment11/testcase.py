import unittest

from src.Assignment11.util import min_max
class MyTestCase(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(3, min_max()) #4 2 2 5 3 7 1 3 4 0

    def testcase2(self):
            self.assertEqual(7, min_max()) #4 2 2 5 8 7 1 4 4 0


if __name__ == '__main__':
    unittest.main()
