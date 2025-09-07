class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for char in s:
            if char == '*':
                del ans[-1]
            else:
                ans.append(char)
        sans = ""
        for char in ans:
            sans += char
        return sans       