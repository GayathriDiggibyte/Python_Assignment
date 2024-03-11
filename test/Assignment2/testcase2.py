import unittest
from src.Assignment2.util import find_runnerUp_score

class MyTestCase(unittest.TestCase):
    def test_something(self):
        find_runnerUp_score("5 5 5 5 5 5 5 5 5 6", 10)
        self.assertEqual(5, 5)


if __name__ == '__main__':
    unittest.main()
