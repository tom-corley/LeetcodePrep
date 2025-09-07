from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Stack of rightwards travelling asteroids, when we meet a left, collide them
        ans = []
        right = []
        for ast in asteroids:
            if ast < 0:
                if not right:
                    ans.append(ast)
                else:
                    while right and right[-1] < abs(ast):
                        right.pop() 
                    if right and right[-1] == abs(ast):
                        right.pop()
                    elif not right:
                        ans.append(ast)
            else:
                right.append(ast)
        ans += right
        return ans