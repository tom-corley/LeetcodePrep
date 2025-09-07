from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Setup
        q = deque()
        q.append([(entrance[0], entrance[1]), 0])
        visited = set()
        visited.add((entrance[0], entrance[1]))
        m = len(maze)
        n = len(maze[0])

        while q:
            # Remove new coordinate from queue
            loc, steps = q.popleft()
            r, c = loc

            # Check if we are at an exit
            if (r != entrance[0] or c != entrance[1]) and ( r == 0 or r == (m - 1) or c == 0 or c == (n-1) ):
                return steps
            
            # Step in all possible directions
            if r > 0 and ((r-1, c) not in visited) and maze[r-1][c]  == ".":
                q.append([(r-1, c), steps+1])
                visited.add((r-1, c))
            if r < m - 1 and ((r+1, c) not in visited) and maze[r+1][c]  == ".":
                q.append([(r+1, c), steps+1])
                visited.add((r+1, c))
            if c > 0 and ((r, c-1) not in visited) and maze[r][c-1]  == ".":
                q.append([(r, c-1), steps+1])
                visited.add((r, c-1))
            if c < (n - 1) and ((r, c+1) not in visited) and maze[r][c+1]  == ".":
                q.append([(r, c+1), steps+1])
                visited.add((r, c+1))
        return -1

