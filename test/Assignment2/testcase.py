import unittest

from src.Assignment2.util import find_runnerUp_score
class MyTestCase(unittest.TestCase):
    def testcase1(self):
        r1=find_runnerUp_score("2 3 6 6 5",5)
        self.assertEqual(5, r1)  # add assertion here

    def testcase2(self):
        r2=find_runnerUp_score("5 5 5 5 5 5 5 5 5 6", 10)
        self.assertEqual(5, r2)

    def testcase3(self):
        r3=find_runnerUp_score("1 -1 -2 -1", 4)
        self.assertEqual(-1, r3)


if __name__ == '__main__':
    unittest.main()
