import unittest
from problem_3 import *

class TestProblem3(unittest.TestCase):
    def test_merge(self):
        merged = merge([7,3,1],[6,5,2])
        self.assertEqual(merged,[7,6,5,3,2,1])

    def test_sort(self):
        arr = [8,3,17,0,10,2]
        sorted = sort(arr)
        self.assertEqual(sorted,[17,10,8,3,2,0])
        self.assertEqual(sort([1,0]),[1,0])
        self.assertEqual(sort([97,98,99]),[99,98,97])
