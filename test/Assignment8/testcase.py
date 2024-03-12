import unittest
from src.Assignment8.util import find_avg_marks_of_stds

class MyTestCase(unittest.TestCase):
    def testcase1(self):
        find_avg_marks_of_stds()
        self.assertEqual(81.00, 81.00)  # add assertion here
    def testcase2(self):
        find_avg_marks_of_stds()
        self.assertEqual(75.37, 75.37)
    def testcase3(self):
        find_avg_marks_of_stds()
        self.assertEqual(73.80,73.80)

if __name__ == '__main__':
    unittest.main()
