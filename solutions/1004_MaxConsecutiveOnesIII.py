from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Sliding Window 
        flips_left = k
        l, r = 0, 0
        ans = 0
        while r < len(nums):
            # Expand right
            if nums[r] == 1:
                ans = max(ans, 1 + r - l)
                r += 1
            elif flips_left > 0:
                flips_left -= 1
                ans = max(ans, 1 + r - l)
                r += 1
            else:
                if nums[l] == 0:
                    flips_left += 1
                l += 1
        return ans
