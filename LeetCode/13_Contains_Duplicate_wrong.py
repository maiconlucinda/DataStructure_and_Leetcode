class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        first_pointer = 0
        second_pointer = 1

        while first_pointer < len(nums) - 1:
            if nums[first_pointer] == nums[second_pointer]:
                return True

            second_pointer += 1

            if second_pointer == len(nums):
                first_pointer += 1
                second_pointer = first_pointer + 1

        return False

solution = Solution()
res = solution.containsDuplicate([1,2,3,4,5,5])


print(res)