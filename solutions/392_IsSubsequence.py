class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Two pointers approach
        i = 0
        j = 0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                j += 1
            i += 1
        return j >= len(s)
        