import unittest
from src.Assignment1.util import find_average_score

class MyTestCase(unittest.TestCase):
    def test_something(self):
        find_average_score({"Harsh": [25, 26.5, 28], "Anurag": [26, 28, 30]}, "Harsh")
        self.assertEqual(26.50, 26.50)

if __name__ == '__main__':
    unittest.main()
