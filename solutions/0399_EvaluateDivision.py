from typing import List
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in connections:
            # Road from u to v
            graph[u].append((v, 1))
            # Reverse road from v to u
            graph[v].append((u, 0))

        def dfs(node, parent):
            change_count = 0
            for neighbor, direction in graph[node]:
                if neighbor != parent:
                    # Count the edges that need to be changed
                    change_count += direction
                    change_count += dfs(neighbor, node)
            return change_count

        return dfs(0, -1)