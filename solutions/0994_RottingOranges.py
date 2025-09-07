from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Count fresh oranges, and add rotting oranges to queue
        q = deque()
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([(i, j), 0])
        
        # Edge case where we start with no fresh oranges
        if fresh == 0:
            return 0
        
        # Run bfs until no rot spreads in a step
        while q:
            # Rot current orange, and if no fresh left stop
            loc, mins = q.popleft()
            r, c = loc
            if grid[r][c] == 1:
                fresh -= 1
                grid[r][c] = 2
            if fresh == 0:
                return mins
            
            # Add all adjacent fresh oranges:
            if r > 0 and grid[r-1][c] == 1:
                q.append([(r-1, c), mins+1])
            if r < m - 1 and grid[r+1][c] == 1:
                q.append([(r+1, c), mins+1])
            if c > 0 and grid[r][c-1] == 1:
                q.append([(r, c-1), mins+1])
            if c < n - 1 and grid[r][c+1] == 1:
                q.append([(r, c+1), mins+1])
        # If not all fresh oranges could be rotten
        return -1
        