from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function on whether a number is possible
        def can_eat(k):
            t = 0
            for pile in piles:
                t += (pile // k)
                if pile % k != 0:
                    t += 1
            return t <= h
        
        # Always possible for big enough k since h >= len(piles)
        l = 1
        r = max(piles) 
        while l < r:
            m = (l+r) // 2
            if can_eat(m):
                r = m
            else:
                l = m + 1
        return l