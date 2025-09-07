from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Minimum in each prefix
        prefix_mins = []
        mn = nums[0]
        for num in nums:
            if num < mn:
                mn = num
            prefix_mins.append(mn)

        # Maximum in each suffix
        suffix_maxs = []
        rev_nums = nums[::-1]
        mx = rev_nums[0]
        for num in rev_nums:
            if num > mx:
                mx = num
            suffix_maxs.append(mx)
        suffix_maxs = suffix_maxs[::-1]

        # For each j check whether min of prefix < nums[j] and max of suffix > nums[j]
        for j in range(1, len(nums) - 1):
            if prefix_mins[j-1] < nums[j] and suffix_maxs[j+1] > nums[j]:
                return True
        return False
        