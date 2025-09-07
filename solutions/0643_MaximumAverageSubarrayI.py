from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Average first k
        avg = 0
        for i in range(k):
            avg += (nums[i] / k)
        ans = avg
        
        # Sliding Window
        for i in range(k, len(nums)):
            avg -= (nums[i-k]/k)
            avg += (nums[i]/k)
            ans = max(ans, avg)
        
        return ans

        