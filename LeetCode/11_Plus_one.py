class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number = int(''.join(map(str, digits))) + 1
        
        return [int(digit) for digit in str(number)]

solution = Solution()
print(solution.plusOne([9]))