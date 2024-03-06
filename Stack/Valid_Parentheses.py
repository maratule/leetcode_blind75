'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine
if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 2:
Input: s = "()[]{}"
Output: true
'''

class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char not in Map:
                stack.append(char)
                continue
            if not stack or stack[-1] != Map[char]:
                return False
            stack.pop()

        return not stack