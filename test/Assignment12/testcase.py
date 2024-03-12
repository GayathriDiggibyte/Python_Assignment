import unittest
from src.Assignment12.util import determinant

class MyTestCase(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(0.0, determinant())  # 2 1.1 1.1 1.1 1.1

    def testcase2(self):
        self.assertEqual(6.0, determinant())  # 3 1 2 3 4 5 6 1 2 1


if __name__ == '__main__':
    unittest.main()
