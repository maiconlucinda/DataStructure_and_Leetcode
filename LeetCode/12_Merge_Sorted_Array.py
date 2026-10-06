class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        
        index = len(nums1) - 1
        for number in reversed(nums2):
            nums1[index] = number
            

            if nums1[index-1] > nums1[index]:
                nums1[index], nums1[index-1] = nums1[index-1], nums1[index]

            index -= 1


        
        print(nums1)
            
    
solution = Solution()

solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)


