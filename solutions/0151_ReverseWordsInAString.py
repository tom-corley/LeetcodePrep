class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        ans = ""
        for i in range(len(words)):
            ans += words[-1-i]
            if i < len(words) - 1:
                ans += " "
        return ans
        