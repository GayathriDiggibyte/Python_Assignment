import unittest

from src.Assignment5.util import print_format_numbers
class MyTestCase(unittest.TestCase):
    def testcase1(self):
        print_format_numbers(2)
        self.assertEqual( "1  1  1  1\n2  2  2 10", "1  1  1  1\n2  2  2 10")  # add assertion here
    def testcase2(self):
        print_format_numbers(17)
        self.assertEqual(" 1     1     1     1\n2     2     2    10\n3     3     3    11\n4     4     4   100\n5     5     5   101\n6     6     6   110\n7     7     7   111\n8    10     8  1000\n9    11     9  1001\n10    12     A  1010\n11    13     B  1011\n12    14     C  1100\n13    15     D  1101\n14    16     E  1110\n15    17     F  1111\n16    20    10 10000\n17    21    11 10001"," 1     1     1     1\n2     2     2    10\n3     3     3    11\n4     4     4   100\n5     5     5   101\n6     6     6   110\n7     7     7   111\n8    10     8  1000\n9    11     9  1001\n10    12     A  1010\n11    13     B  1011\n12    14     C  1100\n13    15     D  1101\n14    16     E  1110\n15    17     F  1111\n16    20    10 10000\n17    21    11 10001")


if __name__ == '__main__':
    unittest.main()
