'''Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.'''

from typing import List

nums = [100,4,200,1,3,2]
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n-1) not in numSet:
                sequence = 1
                while (n + sequence) in numSet:
                    sequence += 1
                longest = max(longest, sequence)

        return longest

mysolution = Solution()
a = mysolution.longestConsecutive(nums)

print(a)
