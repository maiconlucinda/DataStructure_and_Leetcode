
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for index_ex in range(len(nums)):
            print(index_ex)
            for index_in in range(index_ex + 1, len(nums)):
                
                if nums[index_ex] + nums[index_in] == target:
                    return [index_ex, index_in]

        return []

solution = Solution()

print(solution.twoSum([3,2,4], 6))