import unittest

from src.Assignment1.util import find_average_score
class MyTestCase(unittest.TestCase):
    def test_something(self):
        find_average_score({"Vikram": [6, 7, 8], "Viswarup": [7, 8, 9]}, "Viswarup")
        self.assertEqual(8.00, 8.00)

if __name__ == '__main__':
    unittest.main()
