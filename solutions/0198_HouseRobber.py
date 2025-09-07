from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [-1 for _ in range(len(nums))]
        dp[-1] = nums[-1]
        dp[-2] = max(nums[-2], nums[-1])

        for i in range(len(nums) - 3, -1, -1):
            dp[i] = max(dp[i+1], nums[i] + dp[i+2])
        return dp[0]