'''Given an integer array nums, return true
if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:
Input: nums = [1,2,3,1]
Output: true
Example 2:
Input: nums = [1,2,3,4]
Output: false
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = {}

        for i in nums:
            if i in hashmap:
                return True
            else:
                hashmap[i] = 1
        return False


case = Solution()
case.containsDuplicate(nums)