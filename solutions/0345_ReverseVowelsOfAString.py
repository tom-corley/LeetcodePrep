class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        occurences = []
        positions = []

        for i, char in enumerate(s):
            if char in vowels:
                occurences.append(char)
                positions.append(i)
        last = -1
        ans = ""
        for i,index in enumerate(positions):
            ans += s[last+1: index]
            ans += occurences[-1-i]
            last = index
        ans += s[last+1:]
        return ans