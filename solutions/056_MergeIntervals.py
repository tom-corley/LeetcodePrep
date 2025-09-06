from typing import List

class Solution:
    # sort by start, while start of new intervals is less than next
    # extend, or skip- O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        ans = []
        while i < len(intervals):
            intvl = [intervals[i][0], intervals[i][1]]
            j = i + 1
            while j < len(intervals) and intervals[j][0] <= intvl[1]:
                intvl[1] = max(intvl[1], intervals[j][1])
                j += 1   
            ans.append(intvl)
            i = j
        return ans