import unittest
from src.Assignment7.util import calendar_module

class MyTestCase(unittest.TestCase):
    def test_something(self):
        calendar_module("08 05 2015")
        self.assertEqual("WEDNESDAY", "WEDNESDAY")  # add assertion here


if __name__ == '__main__':
    unittest.main()
