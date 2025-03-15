import unittest

from main import *

class Test(unittest.TestCase):

    def test_add(self):
        a = 10
        b = 10
        c = 20
        self.assertEqual(add_1(a, b), c)

if __name__ == '__main__':
    unittest.main()