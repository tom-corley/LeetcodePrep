class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}
        for char in magazine:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        for char in ransomNote:
            if char in freq and freq[char] > 1:
                freq[char] -= 1
            elif char in freq:
                del freq[char]
            else:
                return False
        return True