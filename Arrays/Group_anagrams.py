'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
Input: strs = [""]
Output: [[""]]
'''
from typing import List
from collections import defaultdict
strs = ["","",""]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            count = [0] * 26  # Count occurrences of each character
            for char in word:
                count[ord(char) - ord('a')] += 1
            # Convert count to a tuple to use as a key in the dictionary
            key = tuple(count)
            anagrams[key].append(word)

        return list(anagrams.values())

# Example usage:

solution = Solution()
result = solution.groupAnagrams(strs)
print(result)