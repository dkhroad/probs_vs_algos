import unittest
from problem_2 import *

class TestProblem2(unittest.TestCase):
    def test_pivot_1(self):
        arr = []
        self.assertEqual(find_pivot_index(arr),-1)

    def test_pivot_2(self):
        arr = [10]
        self.assertEqual(find_pivot_index(arr),0)

    def test_pivot_3(self):
        arr = [10,20]
        self.assertEqual(find_pivot_index(arr),1)

    def test_pivot_4(self):
        arr = [10,20,1,3,6,7,8]
        self.assertEqual(find_pivot_index(arr),2)

    def test_binay_search(self):
        arr = []
        self.assertEqual(binary_search(arr,0,0,0),-1)

        arr = [0]
        self.assertEqual(binary_search(arr,0,0,0),0)

        arr = [0]
        self.assertEqual(binary_search(arr,1,0,0),-1)

        arr = [0,1,3]
        self.assertEqual(binary_search(arr,1,0,len(arr)-1),1)


    def test_rotated_array_search(self):
        arr = [10,20,1,3,6,7,8]
        self.assertEqual(rotated_array_search(arr,10),0)
        self.assertEqual(rotated_array_search(arr,3),3)
        self.assertEqual(rotated_array_search(arr,8),6)



