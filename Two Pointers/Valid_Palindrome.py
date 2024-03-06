class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isalpha(c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))

        left, right = 0, len(s)-1

        while right>left:
            while right>left and not isalpha(s[left]):
                left += 1
            while right>left and not isalpha(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


s = "A man, a plan, a canal: Panama"
case = Solution()
print(case.isPalindrome(s))





