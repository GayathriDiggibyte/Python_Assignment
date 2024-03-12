import unittest
from src.Assignment1.util import find_average_score

class MyTestCase(unittest.TestCase):
    def testcase1(self):
        r=find_average_score({"alpha":[20,30,40],"beta":[30,50,70]},"beta")
        self.assertEqual('50.00',r)

    def testcase2(self):
        r=find_average_score({"Harsh": [25, 26.5, 28], "Anurag": [26, 28, 30]}, "Harsh")
        self.assertEqual('26.50',r)

    def testcase3(self):
        r=find_average_score({"Vikram": [6, 7, 8], "Viswarup": [7, 8, 9]}, "Viswarup")
        self.assertEqual('8.00',r)

if __name__ == '__main__':
    unittest.main()
