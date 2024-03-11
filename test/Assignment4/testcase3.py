import unittest

from src.Assignment4.util import merge_the_tools
class MyTestCase(unittest.TestCase):
    def test_something(self):
        merge_the_tools(
            "A",
            1)
        self.assertEqual(
            "A",
            "A")  # add assertion here


if __name__ == '__main__':
    unittest.main()
