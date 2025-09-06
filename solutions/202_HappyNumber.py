class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            n = sum([i*i for i in [int(s) for s in str(n)]])
            if n in seen:
                return False
            seen.add(n)
        return True
        