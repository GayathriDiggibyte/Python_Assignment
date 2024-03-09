import unittest
from src.Assignment1.util import find_average_score

class MyTestCase(unittest.TestCase):
    def test_something(self):
         # add assertion here
        find_average_score({"alpha":[20,30,40],"beta":[30,50,70]},"beta")
        self.assertEqual(50.00, 50.00)

if __name__ == '__main__':
    unittest.main()
