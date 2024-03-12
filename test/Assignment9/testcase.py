import unittest

from src.Assignment9.util import time_delta
class MyTestCase(unittest.TestCase):
    def testcase1(self):
        self.assertEqual('25200\n88200', time_delta("2\nSun 10 May 2015 13:54:36 -0700\nSun 10 May 2015 13:54:36 -0000\nSat 02 May 2015 19:54:36 +0530\nFri 01 May 2015 13:54:36 -0000"))  # add assertion here


if __name__ == '__main__':
    unittest.main()
