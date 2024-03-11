import unittest
from src.Assignment2.util import find_runnerUp_score

class MyTestCase(unittest.TestCase):
    def test_something(self):
        find_runnerUp_score("1 -1 -2 -1", 4)
        self.assertEqual(-1, -1)

if __name__ == '__main__':
    unittest.main()
