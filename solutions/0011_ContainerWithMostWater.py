from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two pointers
        l = 0
        r = len(height) - 1
        ans = (r - l) * min(height[l], height[r])
        while l < r:
            capacity = (r - l) * min(height[l], height[r])
            if capacity > ans:
                ans = capacity
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans