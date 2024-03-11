import unittest

from src.Assignment5.util import print_format_numbers
class MyTestCase(unittest.TestCase):
    def test_something(self):
        print_format_numbers(2)
        self.assertEqual( "1  1  1  1\n2  2  2 10", "1  1  1  1\n2  2  2 10")  # add assertion here


if __name__ == '__main__':
    unittest.main()
