import unittest
from src.Assignment5.util import print_format_numbers

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        expected_output = " 1  1  1  1\n 2  2  2 10"
        self.assertEqual(expected_output, print_format_numbers(2))
        print(print_format_numbers(2))
    def test_case_2(self):
        expected_output = "    1     1     1     1\n    2     2     2    10\n    3     3     3    11\n    4     4     4   100\n    5     5     5   101\n    6     6     6   110\n    7     7     7   111\n    8    10     8  1000\n    9    11     9  1001\n   10    12     A  1010\n   11    13     B  1011\n   12    14     C  1100\n   13    15     D  1101\n   14    16     E  1110\n   15    17     F  1111\n   16    20    10 10000\n   17    21    11 10001"
        self.assertEqual(expected_output, print_format_numbers(17))
        print(print_format_numbers(17))

if __name__ == '__main__':
    unittest.main()
