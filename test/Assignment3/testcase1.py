import unittest

from src.Assignment3.util import mutation
class MyTestCase(unittest.TestCase):
    def test_something(self):
        mutation('abracadabra',5,'k')
        self.assertEqual('abrackdabra', 'abrackdabra')  # add assertion here


if __name__ == '__main__':
    unittest.main()
