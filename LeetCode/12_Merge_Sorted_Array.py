class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        writepointer = m + n - 1
        firstpointer = m
        secondpointer = n

        while firstpointer > 0 and secondpointer > 0:
            if nums1[firstpointer -1] > nums2[secondpointer -1]:
                nums1[writepointer] = nums1[firstpointer -1]
                firstpointer -= 1
            else:
                nums1[writepointer] = nums2[secondpointer -1]
                secondpointer -= 1

            writepointer -= 1


        while secondpointer > 0:
            nums1[writepointer] = nums2[secondpointer -1]
            secondpointer, writepointer = secondpointer -1, writepointer -1

        print(nums1)




solution = Solution()

solution.merge([2,2,3,0,0,0], 3, [1,5,6], 3)