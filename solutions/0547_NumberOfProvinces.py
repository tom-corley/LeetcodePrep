from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        ans = 0
        for i in range(len(isConnected)):
            # If city is not in already traversed connected component, traverse it
            if i not in visited:
                stack = [i]

                while stack:
                    cur = stack.pop()
                    visited.add(cur)
                    for j in range(len(isConnected)):
                        if isConnected[cur][j] and j not in visited:
                            stack.append(j)
                ans += 1
        return ans
