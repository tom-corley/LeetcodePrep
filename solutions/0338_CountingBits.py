from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Optimised solution
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            ## The number of ones except the 2^0 digit plus the 2^0 digit
            dp[i] = dp[i >> 1] + (i & 1)
        return dp



    def countBits2(self, n: int) -> List[int]:
        # O(log(n)) helper function
        def num_ones(i):
            ct = 0
            while i > 0:
                if i % 2 == 1:
                    ct += 1
                i //= 2
            return ct

        # Naive solution, for each i, use a log(n) function to find number of 1s
        ans = []
        for i in range(n+1):
            ans.append(num_ones(i))
        
        return ans
        