class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # Naive solution is count the number of bits where a and c differ, and where b and c differ, take min
        ans = 0
        while a or b or c:
            if c & 1:
                if (a | b) & 1:
                    pass
                else:
                    ans += 1
            else:
                if (a & 1):
                    ans += 1
                if (b & 1):
                    ans += 1
            
            a >>= 1
            b >>= 1
            c >>= 1
        return ans