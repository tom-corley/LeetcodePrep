from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        total_candies = [candies[i] + extraCandies for i in range(len(candies))]
        mx = max(candies)
        ans = [False for _ in range(len(candies))]
        for i in range(len(candies)):
            if total_candies[i] >= mx:
                ans[i] = True
        return ans