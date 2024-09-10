import unittest
#from code1 import add, is_even
from code1 import *

class MyTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
    def test_is_even(self):
        self.assertTrue(is_even(2))

unittest.main()
