from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Naive is O(nm)
        # Sort potions then binary search O((n+m)log m)
        # Want to find the smallest strength potion that is successful
        potions.sort()
        pairs = []

        for spell in spells:
            l = 0
            r = len(potions) - 1
            while l < r:
                m = (l + r) // 2
                prod = spell * potions[m]
                if prod >= success:
                    r = m
                else:
                    l = m + 1
            if l == len(potions) - 1:
                if spell * potions[l] < success:
                    l += 1

            pairs.append(len(potions) - l)
        return pairs