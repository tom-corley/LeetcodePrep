class Solution:
    def numTilings(self, n: int) -> int:
        dp = [-1 for _ in range(n)]
        for i in range(n -1, -1, -1):
            if i == n - 1:
                dp[i] = 1
            elif i == n - 2:
                dp[i] = 2
            elif i == n - 3:
                dp[i] = 5
            else:
                dp[i] = 2 + dp[i+2] + dp[i+1]
                for j in range(i+3, n):
                    dp[i] += 2*dp[j]
        return dp[0] % (10**9 + 7)