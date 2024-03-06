'''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]'''
from typing import List
nums = [1,2,3,4]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1]*len(nums)

        init_prod = 1
        for i in range(len(nums)):
            result[i] = init_prod
            init_prod *= nums[i]
        rev_prod = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= rev_prod
            rev_prod *= nums[i]
        return result
case = Solution()
a = case.productExceptSelf(nums)
print(a)

