from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        l, r = 0, 0
        ans = len(nums)
        total = nums[0]
        while l <= r and r < len(nums):
            if total >= target:
                ans = min((r - l + 1), ans)
                total -= nums[l]
                l += 1
            else:
                if r < len(nums) - 1:
                    r += 1
                    total += nums[r]
                else:
                    break
        return ans