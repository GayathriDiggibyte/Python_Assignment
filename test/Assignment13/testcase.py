import unittest

from src.Assignment13.util import mean_var_std
class MyTestCase(unittest.TestCase):
    def testcase1(self):
        self.assertEqual("[1.5 3.5]\n[1. 1.]\n1.11803398875", mean_var_std())  #2 2 1 2 3 4

    def testcase2(self):
        self.assertEqual("[1. 1. 1.]\n[0. 0. 0.]\n0.0", mean_var_std()) #3 3 1 1 1 1 1 1 1 1 1

if __name__ == '__main__':
    unittest.main()
