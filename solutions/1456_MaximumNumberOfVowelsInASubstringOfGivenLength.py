class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        vowel_ct = 0
        for i in range(k):
            if s[i] in vowels:
                vowel_ct += 1
        ans = vowel_ct
        l, r = 0, k
        while r < len(s):
            if s[l] in vowels:
                vowel_ct -= 1
            if s[r] in vowels:
                vowel_ct += 1
            if vowel_ct > ans:
                ans = vowel_ct
            l += 1
            r += 1
        return ans