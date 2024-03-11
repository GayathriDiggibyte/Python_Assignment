import unittest

from src.Assignment2.util import find_runnerUp_score
class MyTestCase(unittest.TestCase):
    def test_something(self):
        find_runnerUp_score("2 3 6 6 5",5)
        self.assertEqual(5, 5)  # add assertion here


if __name__ == '__main__':
    unittest.main()
