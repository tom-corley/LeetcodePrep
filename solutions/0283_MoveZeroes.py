from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] and not nums[slow]:
                nums[fast], nums[slow] = nums[slow], nums[fast]
            
            if nums[slow] != 0:
                slow += 1
        return nums

    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zeros = 0
        while i < len(nums) - zeros:
            if nums[i] == 0:
                zeros += 1
                del nums[i]
                nums.append(0)
            else:
                i += 1
        return nums