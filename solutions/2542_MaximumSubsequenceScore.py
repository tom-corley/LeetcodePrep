from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [[nums2[i], nums1[i]] for i in range(len(nums1))]
        pairs.sort(reverse = True) # O(nlogn)
        ans = float('-inf')

        if k == 1:
            scores = [nums1[i]*nums2[i] for i in range(len(nums1))]
            return max(scores)

        heap = []
        subsq_sum = 0
        for i in range(len(nums1)):
            if i < k - 1:
                subsq_sum += pairs[i][1]
                heapq.heappush(heap, pairs[i][1])
            else:
                subsq_min = pairs[i][0]
                subsq_cur = pairs[i][1]
                score = (subsq_sum + subsq_cur) * subsq_min
                if score > ans:
                    ans = score
                
                if subsq_cur > heap[0]:
                    subsq_sum -= heapq.heappop(heap)
                    subsq_sum += subsq_cur
                    heapq.heappush(heap, subsq_cur)
        return ans