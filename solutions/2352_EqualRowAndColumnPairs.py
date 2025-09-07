from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        uniq_occ = set()
        for num in freq.keys():
            uniq_occ.add(freq[num])
        return len(uniq_occ) == len(freq.keys())