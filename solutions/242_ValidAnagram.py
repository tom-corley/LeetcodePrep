class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}
        for char in s:
            if char in freq1:
                freq1[char] += 1
            else:
                freq1[char] = 1
        for char in t:
            if char in freq2:
                freq2[char] += 1
            else:
                freq2[char] = 1
        return freq1 == freq2