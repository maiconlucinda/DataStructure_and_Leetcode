

class Solution:
    def isPalindrome(self, x: int) -> bool:
        inverted = str(x)[::-1]

        return inverted == str(x)

result = Solution()

result.isPalindrome(242)