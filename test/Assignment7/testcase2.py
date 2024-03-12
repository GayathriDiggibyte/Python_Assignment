import unittest
from src.Assignment7.util import calendar_module

class MyTestCase(unittest.TestCase):
    def test_something(self):
        calendar_module("04 06 2012")
        self.assertEqual("FRIDAY", "FRIDAY")  # add assertion here


if __name__ == '__main__':
    unittest.main()
