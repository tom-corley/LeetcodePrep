from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by start and break ties with end
        # for each interval, remove all intervals that start before this one ends
        intervals.sort()
        print(intervals)
        removed = 0
        prev = intervals[0]
        i = 1
        while i < len(intervals):
            if intervals[i][0] >= prev[1]:
                prev = intervals[i]
                i += 1
            elif intervals[i][1] >= prev[1]:
                removed += 1
                i += 1
            else:
                removed += 1
                prev = intervals[i]
                i += 1
        
        return removed
        