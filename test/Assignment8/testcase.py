import unittest
from src.Assignment8.util import find_avg_marks_of_stds

class MyTestCase(unittest.TestCase):
    def testcase1(self):
        r=find_avg_marks_of_stds()
        self.assertEqual('81.00', r)  # add assertion here
    def testcase2(self):
        r=find_avg_marks_of_stds()
        self.assertEqual('75.37', r)
    def testcase3(self):
        r=find_avg_marks_of_stds()
        self.assertEqual('73.80',r)

if __name__ == '__main__':
    unittest.main()
