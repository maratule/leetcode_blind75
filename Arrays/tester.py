import unittest
from Product_of_Array_Except_Self import Solution


class TestMySolution(unittest.TestCase):

    def setUp(self):
        self.mysolution = Solution()

    def test_basic_pass(self):
       nums = [1,2,3,4]
       expected = [24, 12, 8, 6]
       self.assertEqual(self.mysolution.productExceptSelf(nums), expected)
    def test_empty_list(self):
       nums = []
       expected = []
       self.assertEqual(self.mysolution.productExceptSelf(nums), expected)

    def test_basic_pass(self):
       nums = [1,2,3,4]
       expected = [24, 12, 8, 6]
       self.assertEqual(self.mysolution.productExceptSelf(nums), expected)

if __name__ == '__name__':
    unittest.main()
