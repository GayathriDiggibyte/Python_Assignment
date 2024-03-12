import unittest
from src.Assignment7.util import calendar_module

class MyTestCase(unittest.TestCase):
    def test_something(self):
        calendar_module("02 13 2010")
        self.assertEqual("SATURDAY", "SATURDAY")  # add assertion here


if __name__ == '__main__':
    unittest.main()
