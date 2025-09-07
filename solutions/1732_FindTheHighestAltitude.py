from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums) - 1

        l = 0
        r = 0
        ans = 0
        deleted = False
        while r < len(nums):
            if nums[r] == 1:
                ans = max(ans, r - l)
                if not deleted:
                    ans = max(ans, r - l + 1)
                r += 1
            elif not deleted:
                deleted = True
                ans = max(ans, r - l)
                r += 1
            else:
                if nums[l] == 0:
                    deleted = False
                l += 1
        return ans
            