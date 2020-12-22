from ordeli_arr import *
import unittest

class Test_OrdEliArray(unittest.TestCase):
    def test_Sort_Array(self):
        actual=Sort_Array([1,2,2,5,5,3,4])
        expected=[1,2,2,3,4,5,5]
        self.assertEqual(expected, actual)
    
    def test_EliminateDuplicate(self):
        actual=EliminateDuplicate([1,2,2,5,5,3,4])
        expected=[1,2,3,4,5]
        self.assertEqual(expected, actual)