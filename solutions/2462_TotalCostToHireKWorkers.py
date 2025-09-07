from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # Run min heap to find cheapest workers
        total_cost = 0
        heap1 = []
        heap2 = []

        # Populate left and right heap
        i = 0
        j = len(costs) - 1
        while i <= j and i < candidates:
            heapq.heappush(heap1, costs[i])
            i += 1
        while j > 0 and j >= i and j >= len(costs) - candidates:
            heapq.heappush(heap2, costs[j])
            j -= 1
        print(heap1)
        print(heap2)
        print(f"i = {i}, j = {j}")
        nxt = 0
        for _ in range(k):
            # Add additional worker from side we picked from last, i - 1 is last added on left side, j + 1 on right
            if i <= j and nxt == 1:
                heapq.heappush(heap1, costs[i])
                i += 1
            elif i <= j and nxt == 2:
                heapq.heappush(heap2, costs[j])
                j -= 1
            
            # Compare hires and pick best
            hire1 = float('inf')
            hire2 = float('inf')
            if heap1:
                hire1 = heapq.heappop(heap1)
            if heap2:
                hire2 = heapq.heappop(heap2)
            if hire1 <= hire2:
                print(hire1)
                total_cost += hire1
                nxt = 1
                heapq.heappush(heap2, hire2)
            else:
                print(hire2)
                total_cost += hire2
                nxt = 2
                heapq.heappush(heap1, hire1)
        
        
        return total_cost