import unittest
from src.Assignment18.util import filter_mail

class MyTestCase(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com'], filter_mail())  # add assertion here
# 3 lara@hackerrank.com brian-23@hackerrank.com britts_54@hackerrank.com
    def testcase2(self):
        self.assertEqual(['iota_98@hackerrank.com'], filter_mail())  # add assertion here
# 2 harsh@gmail iota_98@hackerrank.com

if __name__ == '__main__':
    unittest.main()
