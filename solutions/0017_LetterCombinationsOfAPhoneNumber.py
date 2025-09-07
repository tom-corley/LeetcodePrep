from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        def dfs(chars, i, mp, ans):
            if i == len(digits):
                ans.append("".join(chars))
            else:
                for letter in mp[digits[i]]:
                    chars.append(letter)
                    dfs(chars, i+1, mp, ans)
                    chars.pop()
        mp = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], \
           "5": ['j', 'k', 'l'], "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], \
           "8": ['t', 'u', 'v'], "9": ['w', 'x', 'y', 'z']}
        ans = []
        dfs([], 0, mp, ans)
        return ans